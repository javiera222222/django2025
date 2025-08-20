<template>
<VApp>
  <MenuComponent />
  <VMain>
  <RouterView></RouterView>
</VMain>
  </VApp>
</template>

<script>
import MenuComponent from './components/MenuComponent.vue'

export default {
  name: 'App',
  components: {
    MenuComponent
  }
}
</script>

<style></style>