<template>
  <div>
    <form @submit="addNote">
      <div class="field">
        <input
          type="text"
          class="input is-primary"
          v-model="name"
          name="name"
          placeholder="Name..."
        />
        <textarea
          class="textarea is-primary"
          type="text"
          v-model="content"
          name="content"
          placeholder="Content..."
        />
        <input type="submit" value="Create" class="button is-primary" />
      </div>
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