import BadgeRepository from './BadgeRepository';
import GroupRepository from './GroupRepository';
import EmployeeBadgeRepository from './EmployeeBadgeRepository';
import EmployeeRepository from './EmployeeRepository';



const repositories = {
    'groups': GroupRepository,
    'badges': BadgeRepository,
    'employee-badges': EmployeeBadgeRepository,
    'employees': EmployeeRepository
}
export default {
    get: name => repositories[name]
};