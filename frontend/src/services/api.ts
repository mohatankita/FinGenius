import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api",
});

export const pingServer = async () => {
  const res = await api.get("/ping");
  return res.data;
};
