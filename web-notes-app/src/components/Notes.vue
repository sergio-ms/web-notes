<template>
  <div class="Notes">
    <addNote @add-note="addNote" />
    <div v-for="note in allNotes" :key="note.id">
      <noteItem v-bind:note="note" v-on:del-note="deleteNote" />
    </div>
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
import NoteItem from "@/components/NoteItem";
import AddNote from "@/components/AddNote";
export default {
  name: "Notes",
  components: {
    NoteItem,
    AddNote
  },
  methods: {
    ...mapActions(["fetchNotes"])
  },
  computed: mapGetters(["allNotes"]),
  created() {
    this.fetchNotes();
  }
};
</script>
<style scoped></style>
