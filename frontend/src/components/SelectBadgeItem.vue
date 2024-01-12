<template>
  <div class="row align-items-center no-gutters border-top">
    <div class="col-12">
      <b-button
        id="badge-button"
        v-b-toggle="badgeCollapseId"
        block
        variant="outline-primary"
      >
        <BadgeItem
          class="border-top-0"
          id="badges"
          :key="index"
          :badge="badge"
          :index="index"
        />
      </b-button>

      <b-collapse :id="badgeCollapseId">
        <div class="mx-4 my-2">
          <ValidationProvider v-slot="{ errors, valid }" name="comment">
            <b-form-input
              class="badge-form mb-2"
              :id="inputCommentId"
              type="text"
              v-model="form.comment"
              placeholder="Enter comment"
            ></b-form-input>
            <b-form-invalid-feedback :state="valid"
              ><span v-for="(error, index) in errors" :key="index">{{
                error
              }}</span></b-form-invalid-feedback
            >
          </ValidationProvider>

          <div class="row justify-content-end">
            <div class="col-6">
              <ValidationProvider v-slot="{ errors, valid }" name="isAnonymous">
                <b-form-checkbox
                  :id="inputCheckboxId"
                  type="text"
                  v-model="form.isAnonymous"
                  >Anonymous</b-form-checkbox
                >
                <b-form-invalid-feedback :state="valid"
                  ><span v-for="(error, index) in errors" :key="index">{{
                    error
                  }}</span></b-form-invalid-feedback
                >
              </ValidationProvider>
            </div>

            <div class="col-6 text-right">
              <b-button
                class="edit-button"
                size="sm"
                variant="secondary"
                @click="assignBadge"
                >Save</b-button
              >
            </div>
          </div>
        </div>
      </b-collapse>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";
import BadgeItem from "../components/BadgeItem.vue";
import { ValidationProvider } from "vee-validate";

const EmployeeBadgeRepository = Repository.get("employee-badges");

export default {
  data() {
    return {
      isAssigning: false,
      form: {
        comment: "",
        badge: this.badge.id,
        isAnonymous: false,
      },
    };
  },
  props: {
    employeeId: String,
    badge: Object,
    index: Number,
  },
  components: {
    BadgeItem,
    ValidationProvider,
  },
  computed: {
    inputCommentId: function () {
      return `input-comment-${this.badge.id}`;
    },
    inputCheckboxId: function () {
      return `input-checkbox-${this.badge.id}`;
    },
    badgeCollapseId: function () {
      return `badge-collapse-${this.index}`;
    },
    totalBadges() {
      return this.group.badges.length;
    },
  },
  methods: {
    assignBadge() {
      EmployeeBadgeRepository.assignBadge(this.employeeId, this.form).then(
        (response) => {
          if (response.status == 201) {
            this.$router.push("/");
          }
        }
      );
    },
  },
};
</script>