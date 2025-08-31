import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  return Promise.allSettled([uploadPromise, signUpPromise])
    .then((results) => results.map((res) => ({
      status: res.status,
      value: res.status === 'fulfilled' ? res.value : res.reason,
    })));
}
