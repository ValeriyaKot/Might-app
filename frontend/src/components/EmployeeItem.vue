<template>
  <div class="container border-top no-gutters p-0 m-0">
    <div class="row align-items-center no-gutters">
      <div class="col-6 text-start no-gutters">
        <div class="media">
          <img :src="employee.imageUrl" alt="Avatar" class="avatar" />
          <div class="media-body align-self-center">
            <span id="employee-name"
              >{{ employee.firstName }} {{ employee.lastName }}</span
            >
          </div>
        </div>
      </div>
      <div class="col-5 text-right">
        <img
          v-for="badge in last3Badges"
          v-bind:key="badge.id"
          :src="badge.badge.picture"
          alt="badgeInfoIcon"
          class="badge-info-icon"
        />
        <span v-if="moreThan3Badges" class="mx-2"
          >and <strong>{{ quantityEmployeeBadges }} others</strong></span
        >
      </div>
      <div class="col-1 text-right">
        <b-button variant="outline-transparent" v-b-toggle="employeeCollapseId">
          <b-icon
            class="icon"
            icon="list"
            aria-label="menu"
            variant="secondary"
          ></b-icon>
        </b-button>
      </div>
    </div>

    <b-collapse :id="employeeCollapseId">
      <div
        class="row border-top m-0 py-2 justify-content-end align-items-center"
      >
        <div class="col-8 text-left">
          <b-button
            variant="outline-transparent"
            :href="`/${employee.id}/assign`"
          >
            <b-icon
              class="icon"
              icon="plus"
              aria-label="plus"
              variant="secondary"
            ></b-icon>
          </b-button>
        </div>
        <div class="col-4">
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
      </div>
      <div v-b-scrollspy:scrollspy-badges>
        <div id="scrollspy-badges">
          <EmployeeBadgeItem
            class="border-bottom border-top-0"
            id="employeeBadges"
            v-for="(employeeBadge, index) in employeeBadges"
            :key="employeeBadge.id"
            :badge="employeeBadge"
            :index="index"
          />
        </div>
      </div>
    </b-collapse>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";
import EmployeeBadgeItem from "../components/EmployeeBadgeItem.vue";

const EmployeeBadgeRepository = Repository.get("employee-badges");

export default {
  data() {
    return {
      last3Badges: [],
      searchForm: "",
      employeeBadges: [],
      quantityEmployeeBadges: 0,
    };
  },
  props: {
    groups: Array,
    employee: Object,
    index: Number,
  },

  components: {
    EmployeeBadgeItem,
  },

  computed: {
    employeeCollapseId: function () {
      return `employee-collapse-${this.index}`;
    },
    inputCommentId: function () {
      return `input-comment-${this.index}`;
    },
    inputCheckboxId: function () {
      return `input-checkbox-${this.index}`;
    },
    moreThan3Badges: function () {
      return this.employeeBadges.length > 3;
    },
  },
  methods: {
    search() {
      EmployeeBadgeRepository.search(this.employee.id, this.searchForm).then(
        (response) => {
          this.employeeBadges = response.data;
        }
      );
    },
    
    getEmployeeBadges() {
      EmployeeBadgeRepository.getEmployeeBadges(this.employee.id).then((response) => {
        this.employeeBadges = response.data;
        this.wasActiveEmployeeBadgesMenu = true;
        this.last3Badges = response.data.slice(-3);
        if (response.data.length > 3) {
          this.quantityEmployeeBadges = response.data.length - 3;
        }
      });
    },
  },
  mounted() {
    this.getEmployeeBadges()
  },
};
</script>