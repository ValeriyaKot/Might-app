import Repository from './Repository.js';
const resource = '/group-badges';


export default {
    getForManager() {
        return Repository.get(`${resource}/`);
    },
    get() {
        return Repository.get(`${resource}?is_manager=false`);
    },
    getGroup(id) {
        return Repository.get(`${resource}/${id}/`);
    },
};