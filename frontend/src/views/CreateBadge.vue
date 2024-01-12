<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-10">
        <div id="creation-title" class="border-bottom">
          Add badge to {{ group.name }}
        </div>

        <div class="container border px-0">
          <div class="row align-items-center no-gutters">
            <div class="col-11">
              <div class="media align-items-top">
                <img :src="previewPicture" alt="Avatar" class="badge-picture" />
                <div class="media-body py-2">
                  <ValidationProvider
                    v-slot="{ errors, valid }"
                    name="title"
                    :rules="{ required: true, max: 250 }"
                  >
                    <b-form-input
                      class="badge-form"
                      id="input-1"
                      v-model="form.title"
                      type="text"
                      placeholder="Enter title"
                    ></b-form-input>
                    <b-form-invalid-feedback :state="valid"
                      ><span v-for="(error, index) in errors" :key="index">{{
                        error
                      }}</span></b-form-invalid-feedback
                    >
                  </ValidationProvider>
                  <ValidationProvider
                    v-slot="{ errors, valid }"
                    name="description"
                  >
                    <b-form-input
                      class="badge-form"
                      id="input-2"
                      type="text"
                      v-model="form.description"
                      placeholder="Enter description"
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
                      v-on:click="createBadge"
                      size="sm"
                      variant="secondary"
                      >Save</b-button
                    >
                    <b-button
                      class="edit-button"
                      size="sm"
                      variant="secondary"
                      href="/"
                      >Cancel</b-button
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";

import { ValidationProvider } from "vee-validate";

const GroupRepository = Repository.get("groups");
const BadgeRepository = Repository.get("badges");

export default {
  data() {
    return {
      group: [],
      previewPicture: null,
      form: {
        group: null,
        picture: null,
        title: "",
        description: "",
      },
    };
  },
  components: {
    ValidationProvider,
  },
  methods: {
    getGroup() {
      GroupRepository.getGroup(this.$route.params.groupId).then((response) => {
        this.group = response.data;
      });
    },
    createBadge() {
      let formData = new FormData();
      formData.append("picture", this.form.picture);
      formData.append("title", this.form.title);
      formData.append("description", this.form.description);
      formData.append("group", this.$route.params.groupId);
      BadgeRepository.create(formData).then((response) => {
        if (response.status == 201) {
          this.$router.push("/");
        }
      });
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
  mounted() {
    this.getGroup();
  },
};
</script>