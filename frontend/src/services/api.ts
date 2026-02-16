import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const runAudit = async (url: string) => {
  const res = await API.post("/audit/", { url });
  return res.data;
};
