   <template>
     <div>
       <h2>用户列表</h2>
       <ul>
         <li v-for="user in users" :key="user.id">
           {{ user.username }} ({{ user.email }}) - {{ user.bio }}
         </li>
       </ul>
     </div>
   </template>

   <script>
   import api from '@/services/api';

   export default {
     data() {
       return {
         users: []
       };
     },
     mounted() {
       this.fetchUsers();
     },
     methods: {
       async fetchUsers() {
         try {
           const response = await api.get('users/');
           this.users = response.data;
         } catch (error) {
           console.error('获取用户列表失败:', error);
         }
       }
     }
   };
   </script>