<template>
  <div class="row align-items-center no-gutters border-top">
    <div v-if="!isEditing" class="col-10">
      <BadgeItem
        class="border-top-0"
        id="badges"
        :key="index"
        :badge="badge"
        :index="index"
      />
    </div>
    <div v-else class="col-11">
      <div class="media align-items-top">
        <img :src="previewPicture" alt="Avatar" class="badge-picture" />
        <div class="media-body py-2">
          <ValidationProvider
            v-slot="{ errors, valid }"
            name="title"
            :rules="{ required: true, max: 250 }"
          >
            <b-form-input
              v-model="form.title"
              class="badge-form"
              :id="inputBadgeTitleIndex"
              type="text"
            ></b-form-input>
            <b-form-invalid-feedback :state="valid"
              ><span v-for="(error, index) in errors" :key="index">{{
                error
              }}</span></b-form-invalid-feedback
            >
          </ValidationProvider>
          <ValidationProvider v-slot="{ errors, valid }" name="description">
            <b-form-input
              class="badge-form"
              :id="inputBadgeDescriptionIndex"
              type="text"
              v-model="form.description"
            ></b-form-input>
            <b-form-invalid-feedback :state="valid"
              ><span v-for="(error, index) in errors" :key="index">{{
                error
              }}</span></b-form-invalid-feedback
            >
          </ValidationProvider>
          <ValidationProvider
            v-slot="{ errors, valid }"
            name="picture"
            :rules="{ required: true, image: true }"
          >
            <b-form-file @change="onFileChange" plain></b-form-file>
            <b-form-invalid-feedback :state="valid"
              ><span v-for="(error, index) in errors" :key="index">{{
                error
              }}</span></b-form-invalid-feedback
            >
          </ValidationProvider>
          <div class="container mt-2 m-0 p-0 text-right">
            <b-button
              class="edit-button"
              size="sm"
              variant="secondary"
              v-on:click="editBadge"
              >Save</b-button
            >
            <b-button
              class="edit-button"
              size="sm"
              variant="secondary"
              @click="isEditing = !isEditing"
              >Cancel</b-button
            >
          </div>
        </div>
      </div>
    </div>

    <div v-if="!isEditing" class="col-2 text-right">
      <b-button variant="outline-transparent">
        <b-icon
          @click="isEditing = !isEditing"
          class="icon"
          icon="pencil"
          aria-label="edit"
          variant="secondary"
        ></b-icon>
      </b-button>
      <b-button variant="outline-transparent">
        <b-icon
          class="icon"
          icon="trash"
          aria-label="trash"
          variant="secondary"
          v-on:click="deleteBadge"
        ></b-icon>
      </b-button>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";
import BadgeItem from "../components/BadgeItem.vue";
import { ValidationProvider } from "vee-validate";

const BadgeRepository = Repository.get("badges");

export default {
  data() {
    return {
      isEditing: false,
      previewPicture: null,
      form: {
        picture: null,
        title: "",
        description: "",
        group: null
      },
    };
  },
  props: {
    badge: Object,
    index: Number,
  },
  components: {
    BadgeItem,
    ValidationProvider,
  },

  created() {
      this.form.title = this.badge.title;
      this.form.group = this.badge.group;
      this.form.description = this.badge.description;
      this.previewPicture = this.badge.picture;
  },
  computed: {
    inputBadgeTitleIndex: function () {
      return `input-badge-title-${this.index}`;
    },
    inputBadgeDescriptionIndex: function () {
      return `input-badge-description-${this.index}`;
    },
  },
  methods: {
    deleteBadge() {
      BadgeRepository.delete(this.badge.id).then((response) => {
            if (response.status == 204) {
              this.$router.go("/");
            }
          })
    },
    editBadge() {
      let formData = new FormData();
      formData.append("title", this.form.title);
      formData.append("description", this.form.description);
      formData.append("group", this.form.group);
      console.log(this.form.picture)
      if (this.form.picture != null) {
        formData.append("picture", this.form.picture)
      }
      BadgeRepository.edit(this.badge.id, formData).then((response) => {
            if (response.status == 200) {
              this.$router.go("/");
            }
          })
    },
    edit() {
      this.isEditing = !this.isEditing;
    },
    onFileChange(event) {
      let input = event.target;
      if (input.files && input.files[0]) {
        let reader = new FileReader();
        reader.onload = (e) => {
          this.previewPicture = e.target.result;
          this.form.picture = event.target.files[0];
        };
        reader.readAsDataURL(input.files[0]);
      }
    },
  },
};
</script>