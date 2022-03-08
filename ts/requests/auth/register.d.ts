import { UserRole } from "@ts/user/user.enums";

export type RegisterInput = {
  username: string;
  password: string;
  confirmPassword: string;
  role: UserRole;
};

export type RegisterResponse = {
  message?: string;
};