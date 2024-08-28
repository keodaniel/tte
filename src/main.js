// import { createApp } from 'vue'
// import App from './App.vue'

// createApp(App).mount('#app')

import { createApp } from 'vue';
import App from './App.vue';
import VNetworkGraph from "v-network-graph";
import "v-network-graph/lib/style.css";
// import { VNetworkGraph } from './components/VNetworkGraph';

const app = createApp(App);
app.component('VNetworkGraph', VNetworkGraph);
app.mount('#app');
