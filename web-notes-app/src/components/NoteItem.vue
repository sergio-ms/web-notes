<template>
  <div class="note-item">
    <h3>{{ note.name }}</h3>
    <p>{{ note.content }}</p>
    <button @click="this.$emit('del-note', note.id)" class="del">x</button>
  </div>
</template>
<script>
export default {
  name: "NoteItem",
  props: ["note"]
};
</script>
<style scoped></style>
