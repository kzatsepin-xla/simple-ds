import type { InputHTMLAttributes } from "react";
import "./Input.css";

export type InputState = "default" | "error" | "disabled";
export type InputValueType = "default" | "placeholder";

export interface InputProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, "size" | "disabled"> {
  state?: InputState;
  valueType?: InputValueType;
  disabled?: boolean;
  label?: string;
  helperText?: string;
}

export function Input({
  state = "default",
  valueType = "default",
  disabled = false,
  label,
  helperText,
  className = "",
  ...rest
}: InputProps) {
  const visualState: InputState = disabled ? "disabled" : state;
  const wrapperClass = [
    "sds-input-field",
    `sds-input-field--${visualState}`,
    `sds-input-field--${valueType}`,
    className
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <label className={wrapperClass}>
      {label ? <span className="sds-input-field__label">{label}</span> : null}
      <input className="sds-input-field__control" disabled={visualState === "disabled"} {...rest} />
      {helperText ? <span className="sds-input-field__helper">{helperText}</span> : null}
    </label>
  );
}
