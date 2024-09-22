<template>
  <div class="user-registration">
    <h2>用户注册</h2>
    <form @submit.prevent="registerUser">
      <div class="form-group">
        <input id="username" v-model="user.username" type="text" placeholder="用户名" required>
      </div>
      <div class="form-group">
        <input id="email" v-model="user.email" type="email" placeholder="邮箱" required>
      </div>
      <div class="form-group">
        <input id="password" v-model="user.password" type="password" placeholder="密码" required>
      </div>
      <div class="form-group">
        <textarea id="bio" v-model="user.bio" placeholder="个人简介"></textarea>
      </div>
      <div class="form-group">
        <input id="birth_date" v-model="user.birth_date" type="date" placeholder="出生日期">
      </div>
      <button type="submit">注册</button>
    </form>
  </div>
</template>

<script>
    import api from '@/services/api';

    export default {
        data() {
        return {
            user: {
            username: '',
            email: '',
            password: '',
            bio: '',
            birth_date: ''
            }
        };
        },
        methods: {
        async registerUser() {
                try {
                    console.log('Sending registration request:', this.user);
                    const response = await api.post('users/', this.user);
                    console.log('Registration response:', response);
                    alert('用户注册成功');
                    this.$emit('user-registered');
                } catch (error) {
                    console.error('Registration error:', error);
                    if (error.response) {
                    console.error('Error response:', error.response.data);
                    console.error('Error status:', error.response.status);
                    alert('注册失败: ' + JSON.stringify(error.response.data));
                    } else if (error.request) {
                    console.error('No response received:', error.request);
                    alert('注册失败: 未收到服务器响应');
                    } else {
                    console.error('Error setting up request:', error.message);
                    alert('注册失败: ' + error.message);
                    }
                }
            }
        }
    };
</script>

<style scoped>
    .user-registration {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    }

    .form-group {
    margin-bottom: 15px;
    position: relative;
    }

    input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
    }

    textarea {
    height: 100px;
    }

    input::placeholder, textarea::placeholder {
    color: #999;
    }

    button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    }

    button:hover {
    background-color: #45a049;
    }
</style>