<template>
  <div class="container border-top no-gutters p-0 m-0">
    <div class="row align-items-center no-gutters">
      <div class="col-9 text-start no-gutters">
        <div class="media">
          <GroupAvatarItem :icon="group.icon" :key="group.id" />
          <div class="media-body align-self-center">
            <span id="employee-name">{{ group.name }}</span>
          </div>
        </div>
      </div>
      <div class="col-3 text-right">
        <b-button variant="outline-transparent" v-b-toggle="groupCollapseId">
          <b-icon
            class="icon"
            icon="list"
            aria-label="menu"
            variant="secondary"
          ></b-icon>
        </b-button>
      </div>
    </div>

    <b-collapse :id="groupCollapseId">
      <div class="border-top">
        <div class="row align-items-center">
          <div class="col-3 text-start px-4">
            <span id="badges">Badges</span>
          </div>

          <div class="col-9 text-right">
            <b-button variant="outline-transparent">
              <b-icon
                class="icon"
                icon="plus"
                aria-label="plus"
                variant="secondary"
              ></b-icon>
            </b-button>
          </div>
        </div>

        <BadgeItem
          id="groupBadges"
          v-for="badge in group.badges"
          :key="badge.id"
          :badge="badge"
        />
      </div>
    </b-collapse>
  </div>
</template>

<script>
import BadgeItem from "../components/BadgeItem.vue";
import GroupAvatarItem from "../components/GroupAvatarItem.vue";

export default {
  data() {
    return {};
  },
  props: {
    group: Object,
    index: Number,
  },

  components: {
    BadgeItem,
    GroupAvatarItem,
  },

  computed: {
    groupCollapseId: function () {
      return `group-collapse-${this.index}`;
    },
  },
};
</script>