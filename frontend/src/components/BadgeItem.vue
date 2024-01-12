<template>
  <div class="row align-items-center no-gutters border-top">
    <div class="media align-items-center">
      <img :src="badge.picture" alt="badge-picture" class="badge-picture" />
      <div class="media-body py-2 pr-2">
        <span id="badge-title">{{ badge.title }}</span>
        <p id="badge-description">
          {{ badge.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    badge: Object,
    index: Number,
  },
};
</script>