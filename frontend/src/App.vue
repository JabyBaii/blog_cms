<template>
  <!--<img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  <div id="app">
    <UserRegistration @user-registered="refreshUserList" />
    <UserList ref="userList" />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import UserRegistration from '@/components/UserRegistration.vue';
import UserList from '@/components/UserList.vue';

export default {
  name: 'App',
  components: {
    // HelloWorld,
    UserRegistration,
    UserList
  },
  methods: {
    refreshUserList() {
      this.$refs.userList.fetchUsers();
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
