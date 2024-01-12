<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 p-0">
        <b-button id="btn-back" variant="outline-transparent" href="/">
          <b-icon class="pr-1" icon="arrow-left" aria-label="back"></b-icon
          >Back</b-button
        >
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-10">
        <div id="creation-title" class="border-bottom">
          Assign badge to {{ employeeInfo.firstName }}
          {{ employeeInfo.lastName }}
        </div>

        <div class="container border px-0">
          <b-tabs pills card vertical>
            <BadgeGroupItem
              class="p-0"
              id="library"
              v-for="(group, index) in groups"
              v-bind:key="group.id"
              :group="group"
              :index="index"
              :employeeId="employeeId"
            />
          </b-tabs>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";
import BadgeGroupItem from "../components/BadgeGroupItem.vue";

const GroupRepository = Repository.get("groups");
const EmployeeRepository = Repository.get("employees");

export default {
  data() {
    return {
      position: "",
      employeeInfo: [],
      employeeId: this.$route.params.employeeId,
      groups: [],
    };
  },
  props: {},
  components: {
    BadgeGroupItem,
  },
  computed: {
    isManager: function () {
      return this.position === "Group Manager";
    },
  },
  methods: {
    getEmployeeInfo() {
      EmployeeRepository.getInfo(this.employeeId).then((response) => {
        this.employeeInfo = response.data;
      });
    },
    getGroups() {
      if (this.isManager) {
        GroupRepository.getForManager().then((response) => {
          this.groups = response.data;
        });
      } else if (!this.isManager) {
        GroupRepository.get().then((response) => {
          this.groups = response.data;
        });
      }
    },
  },
  mounted() {
    this.getEmployeeInfo(),
    this.getGroups()
  },
};
</script>