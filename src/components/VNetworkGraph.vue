

<script setup>
import { reactive, ref } from 'vue';
import { VNetworkGraph } from 'v-network-graph';
import * as vNG from "v-network-graph";


const initialConfigs = vNG.defineConfigs({
  node : {
    label: {
      visible: true,
      direction: "south",
      directionAutoAdjustment: false
    }
  }
})

const configs = reactive(initialConfigs)

const nodes = ref({
  node1: { name: "SW_NOC" },
  node2: { name: "SW_BnA" },
  node3: { name: "SW_BnB" }
})

const edges = ref({
  edge1: { source: "node1", target: "node2" },
  edge2: { source: "node1", target: "node3" },
  edge3: { source: "node2", target: "node3" }
})

const layouts = ref({
  nodes: {
    node1: { x: 0, y: 0 },
    node2: { x: -100, y: 100 },
    node3: { x: 100, y: 100 }
  }
})

</script>

<template>
  <div>
    <h1>Network Graph</h1>
  </div>
  <div class="demo-control-panel">
    <el-checkbox v-model="configs.node.label.directionAutoAdjustment">Enable auto adjustment</el-checkbox>
  </div>
  <v-network-graph
    class="graph"
    :nodes="nodes"
    :edges="edges"
    :layouts="layouts"
    :configs="configs"
  />
</template>

<style>
.graph {
  width: 500px;
  height: 300px;
  border: 1px solid #000;
  margin: 0 auto; /* Add this line to center the graph */
}
</style>
