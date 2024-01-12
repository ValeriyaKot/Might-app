import Repository from './Repository.js';
const resource = '/employees';
const baseUrl = 'https://wsa-118-61/api/v1'

export default {
    get(currentPage) {
        return Repository.get(`${baseUrl}${resource}?PageSize=10&PageIndex=${currentPage}`);
    },
    getInfo(id) {
        return Repository.get(`${baseUrl}${resource}/${id}`);
    },
};