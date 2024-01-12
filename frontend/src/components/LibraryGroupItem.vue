<template>
  <b-tab :title="group.name">
    <div
      class="row justify-content-end align-items-center no-gutters py-2 pr-2"
    >
      <div class="col-8 text-left">
        <b-button variant="outline-transparent" :href="`/${group.id}/add`">
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
    <div class="border-bottom">
      <LibraryItem
        id="library"
        :per-page="perPage"
        :current-page="currentPage"
        v-for="(badge, index) in badgesForList"
        :key="badge.id"
        :badge="badge"
        :index="index"
      />
    </div>
    <div class="row justify-content-center no-gutters py-3">
      <b-pagination
        v-model="currentPage"
        :total-rows="totalBadges"
        :per-page="perPage"
        aria-controls="library"
      ></b-pagination>
    </div>
  </b-tab>
</template>

<script>
import Repository from "../repositories/RepositoryFactory.js";
import LibraryItem from "./LibraryItem.vue";

const BadgeRepository = Repository.get("badges");

export default {
  data() {
    return {
      badges: this.group.badges,
      perPage: 5,
      currentPage: 1,
      searchForm: "",
    };
  },
  props: {
    group: Object,
    index: Number,
  },

  components: {
    LibraryItem,
  },

  computed: {
    groupCollapseId: function () {
      return `group-collapse-${this.index}`;
    },
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