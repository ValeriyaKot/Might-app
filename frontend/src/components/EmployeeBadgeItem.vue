<template>
  <div class="row align-items-center no-gutters border-top">
    <div class="col-11">
      <div class="media align-items-center">
        <img :src="badge.badge.picture" alt="Avatar" class="badge-picture" />
        <div class="media-body py-2 pr-2">
          <strong id="badge-title">{{ badge.badge.title }}</strong>
          <p class="mb-3" id="badge-description">
            {{ badge.badge.description }}
          </p>
          <p
            v-if="!badge.isAnonymous"
            id="badge-description"
            class="border-bottom pb-1"
          >
            <img
              :src="employeeInfo.imageUrl"
              alt="Avatar"
              class="badge-info-icon"
            />
            <i id="giver-name">
              {{ employeeInfo.firstName }} {{ employeeInfo.lastName }}</i
            >
          </p>
          <i id="comment">{{ badge.comment }}</i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";

const EmployeeRepository = Repository.get("employees");

export default {
  data() {
    return {
      employeeInfo: [],
    };
  },
  props: {
    badge: Object,
  },
  methods: {
    getEmployee() {
      EmployeeRepository.getInfo(this.badge.giver_guid).then((response) => {
        this.employeeInfo = response.data;
      });
    },
  },
  mounted() {
    this.getEmployee();
  },
};
</script>