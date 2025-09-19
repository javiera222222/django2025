<template>
  <v-sheet height="100vh">
    <v-calendar
      v-model="focus"
      :events="events"
      type="month"
      :event-color="() => '#94618e'"
    >
      <template #event="slotProps">
        <div class="event-link">{{ slotProps.event.name }}</div>
      </template>
    </v-calendar>
  </v-sheet>
</template>

<script setup>
import { ref } from 'vue'

const focus = ref(new Date().toISOString().substr(0, 10))

const events = ref([
  { id: 1, name: 'Habitación 101 - Juan', start: '2025-09-10', end: '2025-09-12' },
  { id: 2, name: 'Habitación 102 - Ana', start: '2025-09-11', end: '2025-09-15' }
])
</script>

<style scoped>
.event-link {
  background-color: #94618e;
  color: #f4decb;
  padding: 4px 6px;
  border-radius: 6px;
  font-size: 0.8rem;
}
</style>
