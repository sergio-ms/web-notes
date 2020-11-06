import axios from 'axios';

const state = {
    notes: []
}
const getters = {
    allNotes: state => state.notes
};

const actions = {
    async fetchNotes({ commit }) {
        const response = await axios.get('/api/v1/notes');
        commit('setNotes', response.data)
    },
    async addNote({ commit }, note) {
        const response = await axios
            .post('/api/v1/notes', {
                name: note.name,
                content: note.content
            });
        commit('newNote', response.data);
    },
    async deleteNote({ commit }, id) {
        const response = await axios
            .delete(`/api/v1/notes/${id}`);
        commit('delNote', response.data.id);
    }
}

const mutations = {
    setNotes: (state, notes) => (state.notes = notes),
    newNote: (state, note) => state.notes.unshift(note),
    delNote: (state, id) => (state.notes = state.notes.filter(note => note.id !== id))

}

export default {
    state,
    getters,
    actions,
    mutations
}