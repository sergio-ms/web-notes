<template>
  <div class="note-item">
    <article class="message is-info">
      <div class="message-header">
        <p>{{ note.name }}</p>
        <button
          @click="this.$emit('del-note', note.id)"
          class="delete"
          aria-label="delete"
        ></button>
      </div>
      <div class="message-body">
        {{ note.content }}
      </div>
    </article>
  </div>
</template>
<script>
export default {
  name: "NoteItem",
  props: ["note"]
};
</script>
<style scoped></style>
