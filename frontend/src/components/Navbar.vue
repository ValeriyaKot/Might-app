<template>
  <div>
    <b-navbar class="py-0 pr-0" type="dark" variant="primary">
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <div class="d-flex flex-column align-self-center text-right">
            <p id="user-name">{{ firstName }} {{ lastName }}</p>
            <p id="position">{{ position }}</p>
          </div>
          <b-nav-item-dropdown right no-caret>
            <template #button-content>
              <img class="avatar" :src="picture" />
            </template>
            <b-dropdown-item
              class="text-center"
              @click="login"
              v-if="!isLoggedIn"
              >Login</b-dropdown-item
            >
            <b-dropdown-item
              class="text-center"
              @click="logout"
              v-if="isLoggedIn"
              >Logout</b-dropdown-item
            >
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import AuthService from "../services/auth.service";

const auth = new AuthService();

@Component({
  components: {},
})
class Home extends Vue {
  firstName: string = "";
  lastName: string = "";
  picture: string = "";
  position: string = "";
  accessTokenExpired: boolean | undefined = false;
  isLoggedIn: boolean = false;
  user: Object = {};

  login() {
    auth.login();
  }

  logout() {
    auth.logout();
  }

  mounted() {
    auth.getUser().then((user: any) => {
      if (user) {
        this.firstName = user.profile.name;
        this.lastName = user.profile.family_name;
        this.picture = user.profile.picture;
        this.position = user.profile.position;
        this.accessTokenExpired = user.expired;
        this.isLoggedIn = user !== null && !user.expired;
        this.user = user;
      }
    });
  }
}

export default Home;
</script>