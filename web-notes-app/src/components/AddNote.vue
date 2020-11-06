<template>
  <div>
    <form @submit="onSubmit">
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
import { mapActions } from "vuex";
export default {
  name: "AddNote",
  data() {
    return {
      name: "",
      content: ""
    };
  },
  methods: {
    ...mapActions(["addNote"]),
    onSubmit(e) {
      e.preventDefault();
      const note = {
        name: this.name,
        content: this.content
      };

      this.addNote(note);
    }
  }
};
</script>
<style scoped>
</style>