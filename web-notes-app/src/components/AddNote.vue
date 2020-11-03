<template>
  <div>
    <form @submit="addNote">
      <input type="text" v-model="name" name="name" placeholder="Add note..." />
      <input
        type="text"
        v-model="content"
        name="content"
        placeholder="Content..."
      />
      <input type="submit" value="sbumit" class="btn" />
    </form>
  </div>
</template>
<script>
import uuid from "uuid";
export default {
  name: "AddNote",
  data() {
    return {
      name: "",
      content: ""
    };
  },
  methods: {
    addNote(e) {
      e.preventDefault();
      const newNote = {
        id: uuid.v4(),
        name: this.name,
        content: this.content
      };

      this.$emit("add-note", newNote);
      (this.name = ""), (this.content = "");
    }
  }
};
</script>
<style scoped>
</style>