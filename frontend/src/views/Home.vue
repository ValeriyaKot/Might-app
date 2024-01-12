<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-10">
        <b-tabs v-model="tabIndex" content-class="mt-2">
          <b-tab title="My badges">
            <div class="container border border-top-0 px-0">
              <EmployeeBadgeItem
                id="userBadges"
                :per-page="perMyBadgesPage"
                :current-page="currentMyBadgesPage"
                v-for="(userBadge, index) in userBadgesForList"
                :key="userBadge.id"
                :badge="userBadge"
                :index="index"
              />
            </div>
            <div class="container overflow-auto">
              <div class="row justify-content-center">
                <b-pagination
                  v-model="currentMyBadgesPage"
                  :total-rows="totalUserBadges"
                  :per-page="perMyBadgesPage"
                  aria-controls="userBadges"
                ></b-pagination>
              </div>
            </div>
          </b-tab>
          <b-tab title="Employees">
            <div class="container border border-top-0 px-0">
              <EmployeeItem
                id="employees"
                :current-page="currentPage"
                v-for="(employee, index) in employees"
                :key="employee.id"
                :employee="employee"
                :index="index"
                :groups="groups"
              />
            </div>
            <div class="container overflow-auto">
              <div class="row justify-content-center">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="totalEmployees"
                  :per-page="perPage"
                  aria-controls="employees"
                  @input="changePage"
                ></b-pagination>
              </div>
            </div>
          </b-tab>
          <b-tab v-if="isManager" title="Library">
            <div class="container border px-0">
              <b-tabs pills card vertical>
                <LibraryGroupItem
                  class="p-0"
                  id="library"
                  v-for="(group, index) in groups"
                  v-bind:key="group.id"
                  :group="group"
                  :index="index"
                />
              </b-tabs>
            </div>
          </b-tab>
          <template v-if="tabIndex === 0" #tabs-end>
            <div class="ml-auto">
              <b-input-group>
                <b-form-input
                  v-model="searchForm"
                  size="sm"
                  placeholder="Search"
                ></b-form-input>
                <b-input-group-append>
                  <b-button @click="search" size="sm" variant="primary">
                    <b-icon
                      class="searchIcon"
                      icon="search"
                      aria-label="search"
                    ></b-icon>
                  </b-button>
                </b-input-group-append>
              </b-input-group>
            </div>
          </template>
        </b-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";
import EmployeeBadgeItem from "../components/EmployeeBadgeItem.vue";
import EmployeeItem from "../components/EmployeeItem.vue";
import LibraryGroupItem from "../components/LibraryGroupItem.vue";
import AuthService from "../services/auth.service";

const GroupRepository = Repository.get("groups");
const EmployeeBadgeRepository = Repository.get("employee-badges");
const EmployeeRepository = Repository.get("employees");

export default {
  name: "Home",

  data() {
    return {
      tabIndex: 1,
      searchForm: "",
      position: "",
      userId: "",
      userBadges: [],
      employees: [],
      perPage: 10,
      perMyBadgesPage: 5,
      currentPage: 1,
      currentMyBadgesPage: 1,
      totalEmployees: null,
      groups: [],
    };
  },

  components: {
    EmployeeItem,
    LibraryGroupItem,
    EmployeeBadgeItem,
  },
  computed: {
    totalUserBadges() {
      return this.userBadges.length;
    },
    isManager: function () {
      return this.position === "Group Manager";
    },
    userBadgesForList() {
      return this.userBadges.slice(
        (this.currentMyBadgesPage - 1) * this.perMyBadgesPage,
        this.currentMyBadgesPage * this.perMyBadgesPage
      );
    },
  },
  methods: {
    getGroups() {
      GroupRepository.getForManager().then((response) => {
        this.groups = response.data;
      });
    },
    getUserBadges() {
      EmployeeBadgeRepository.getEmployeeBadges(this.userId).then(
        (response) => {
          this.userBadges = response.data;
        }
      );
    },
    search() {
      EmployeeBadgeRepository.search(this.userId, this.searchForm).then(
        (response) => {
          this.userBadges = response.data;
        }
      );
    },
    changePage() {
      EmployeeRepository.get(this.currentPage).then((response) => {
        this.employees = response.data["items"];
        this.currentPage = response.data["pageIndex"];
        this.totalEmployees = response.data["totalItems"];
      });
    },
  },
  mounted() {
    let _this = this;
    let auth = new AuthService();
    auth.getUser().then(function (user) {
      _this.position = user.profile.position;
      _this.userId = user.profile.sub;
      _this.changePage(), _this.getGroups(), _this.getUserBadges();
    });
  },
};
</script>