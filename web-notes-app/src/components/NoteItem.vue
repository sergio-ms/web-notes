<template>
  <div class="note-item">
    <article class="message is-info">
      <div class="message-header">
        <p>{{ note.name }}</p>
        <button
          @click="deleteNote(note.id)"
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
import { mapActions } from "vuex";
export default {
  name: "NoteItem",
  props: ["note"],
  methods: {
    ...mapActions(["deleteNote"])
  }
};
</script>
<style scoped></style>
