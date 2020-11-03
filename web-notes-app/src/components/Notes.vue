<template>
  <div class="Notes">
    <addNote @add-note="addNote" />
    <div :key="note.id" v-for="note in notes">
      <noteItem v-bind:note="note" v-on:del-note="deleteNote" />
    </div>
  </div>
</template>
<script>
import NoteItem from "@/components/NoteItem";
import AddNote from "@/components/AddNote";
import axios from "axios";
export default {
  name: "Notes",
  components: {
    NoteItem,
    AddNote
  },
  data() {
    return {
      notes: []
    };
  },
  methods: {
    deleteNote(id) {
      axios
        .delete("/api/v1/note/" + id)
        .then(res =>
          this.notes.push(
            (this.notes = this.notes.filter(note => note.id !== res.data.id))
          )
        )
        .catch(err => console.log(err));
    },
    addNote(newNote) {
      const { id, name, content } = newNote;
      console.log(newNote);
      axios
        .post("/api/v1/notes", {
          id,
          name,
          content
        })
        .then(res => this.notes.push(res.data))
        .catch(err => console.log(err));
    }
  },
  created() {
    axios
      .get("/api/v1/notes")
      .then(res => (this.notes = res.data))
      .catch(err => console.log(err));
  }
};
</script>
<style scoped></style>
