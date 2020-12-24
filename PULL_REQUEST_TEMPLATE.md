## Check-list


### General
- [ ] Manual test -> correctness
- [ ] Easy to understand?
- [ ] Coding style and conventions
  - Naming
- [ ] Duplications?
- [ ] Git:
  - Commit messages
  - Meaningful commits (If Not, Squash commits)
- [ ] Can any of the code be replaced with library or built-in functions?


### Documentaion
- [ ] :
  - Readme
  - API
  - TODO list (technical debts)
  - requirements


### Infrastructure
- [ ] DB changes:
  -  Zero down-time
  -  Meaningful migration files
- [ ] Kuber configs:
  - Update secrets
  - Update configMap
  - Update gitlab-ci for new jobs
- [ ] Monitoring:
  - Mention related metrics on description(considering side-effects and service quality)

### Testing
- [ ] Unit-test
- [ ] Checking coverage
- [ ] Staging test
- [ ] Check effects:
  - Other functions on this serviecs
  - Other services


### Review flow
- [ ] First :+1:
  - Run manually
  - Check alternates (implementation, architecture)
  - Comment
    Code should be
      1-Functional
      2-Clean and maintainable
      3-Optimized third.
- [ ] Second :+1:
  - Check alternates and comments
- [ ] Resolve all comments


