<template>
  <div class="hello">
    <h1>{{ message }}</h1>
    <button @click="fetchData">Fetch Data</button>
    <button @click="sendAction">Send Action</button>
    <button @click="getSwitches">Get Switches</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data() {
    return {
      message: '',
    };
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:5000/api/data');
        this.message = response.data.message;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async sendAction() {
      try {
        const response = await axios.post('http://localhost:5000/api/action', { key: 'value' });
        this.message = response.data.status;
        console.log('Action response:', response.data);
      } catch (error) {
        console.error('Error sending action:', error);
      }
    },
    async getSwitches() {
      try {
        const response = await axios.get('http://localhost:5000/api/onosswitches');
        this.message = response.data;
        console.log('Switches:', response.data);
      } catch (error) {
        console.error('Error fetching switches:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
