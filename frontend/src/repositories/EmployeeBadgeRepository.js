import Repository from './Repository.js';
const resource = '/employee-badges';

export default {
    getEmployeeBadges(id) {
        return Repository.get(`${resource}/${id}/`);
    },
    search(id, searchForm) {
        return Repository.get(`${resource}/${id}?search=${searchForm}`);
    },
    assignBadge(id, form) {
        return Repository.post(`${resource}/${id}/`, form);
    },
};