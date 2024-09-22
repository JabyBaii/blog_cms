import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',    // 假设 Django 后端运行在 8000 端口
  withCredentials: true,                    // 允许跨域请求携带 cookies
});

// 添加请求拦截器来设置 CSRF 令牌
api.interceptors.request.use(function (config) {
    const csrfToken = getCookie('csrftoken');
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
  }, function (error) {
    return Promise.reject(error);
  });
  
  // 获取 CSRF 令牌的函数
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

export default api;