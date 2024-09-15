<template>
  <div class="hello">
    <body>Message: {{ message }}</body>
    <!-- <button @click="fetchData">Fetch Data</button> -->
    <!-- <button @click="sendAction">Send Action</button> -->
    <button @click="getSwitches">Get Switches</button>
    <button @click="toggleFwd">Toggle</button>
    <h3 v-if="isReactiveForwardingEnabled.value">Reactive Forwarding Activated</h3>
    <h3 v-else>Reactive Forwarding Deactivated</h3>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: 'HelloWorld',
  data() {
    return {
      message: '',
    };
  },
  computed: {
    isReactiveForwardingEnabled() {
      return ref(false);
    },
  },
  methods: {
    // async fetchData() {
    //   try {
    //     const response = await axios.get('http://localhost:5000/api/data');
    //     this.message = response.data.message;
    //   } catch (error) {
    //     console.error('Error fetching data:', error);
    //   }
    // },
    // async sendAction() {
    //   try {
    //     const response = await axios.post('http://localhost:5000/api/action', { key: 'value' });
    //     this.message = response.data.status;
    //     console.log('Action response:', response.data);
    //   } catch (error) {
    //     console.error('Error sending action:', error);
    //   }
    // },
    async getSwitches() {
      try {
        const response = await axios.get('http://localhost:5000/api/onosswitches');
        this.message = response.data;
        console.log('Switches:', response.data);
      } catch (error) {
        console.error('Error fetching switches:', error);
      }
    },
    async toggleFwd() {
      // this.awesome.value = !this.awesome.value;
      // console.log('Toggle Fwd:', this.awesome.value);
      let app_action
      if (this.isReactiveForwardingEnabled.value) {
        app_action = "deactivate";
      } else {
        app_action = "activate";
      }
      try {
        const response = await axios.post('http://localhost:5000/api/fwd', { action: app_action});
        this.message = response.data;
        console.log('Toggle Fwd:', response.data);
        this.isReactiveForwardingEnabled.value = !this.isReactiveForwardingEnabled.value;
      } catch (error) {
        console.error('Error toggling fwd:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
