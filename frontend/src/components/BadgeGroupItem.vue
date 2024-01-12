<template>
  <b-tab :title="group.name">
    <div
      class="row justify-content-end align-items-center no-gutters py-2 pr-2"
    >
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
    <div class="border-bottom">
      <SelectBadgeItem
        :per-page="perPage"
        :current-page="currentPage"
        id="badges"
        v-for="(badge, index) in badgesForList"
        :key="badge.id"
        :badge="badge"
        :index="index"
        :employeeId="employeeId"
        @changeBadgeId="changeBadgeId"
      />
    </div>
    <div class="row justify-content-center no-gutters py-3">
      <b-pagination
        v-model="currentPage"
        :total-rows="totalBadges"
        :per-page="perPage"
        aria-controls="badges"
      ></b-pagination>
    </div>
  </b-tab>
</template>
<script>
import Repository from "../repositories/RepositoryFactory.js";
import SelectBadgeItem from "../components/SelectBadgeItem.vue";

const BadgeRepository = Repository.get("badges");

export default {
  data() {
    return {
      showAll: true,
      badges: this.group.badges,
      searchForm: "",
      perPage: 5,
      currentPage: 1,
      badgeId: null,
    };
  },
  props: {
    employeeId: String,
    group: Object,
    index: Number,
  },
  components: {
    SelectBadgeItem,
  },
  computed: {
    totalBadges() {
      return this.group.badges.length;
    },
    badgesForList() {
      return this.badges.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage
      );
    },
  },
  methods: {
    changeBadgeId(data) {
      this.badgeId = data;
      this.$emit("changeBadgeId", {
        badgeId: this.badgeId.badgeId,
      });
    },
    search() {
      BadgeRepository.searchInGroup(this.group.id, this.searchForm).then(
        (response) => {
          this.badges = response.data;
        }
      );
    },
  },
};
</script>