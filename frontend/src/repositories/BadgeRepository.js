import Repository from './Repository.js';
const resource = '/badges';

export default {
    get() {
        return Repository.get(`${resource}/`);
    },
    create(formData) {
        return Repository.post(`${resource}/`, formData);
    },
    edit(id, formData) {
        return Repository.patch(`${resource}/${id}/`, formData);
    },
    delete(id) {
        return Repository.delete(`${resource}/${id}/`)
    },
    searchInGroup(groupId, searchForm) {
        return Repository.get(`${resource}/?group=${groupId}&search=${searchForm}`)

    }
};