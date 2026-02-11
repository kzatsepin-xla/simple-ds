import { useEffect, useRef } from "react";
import type { InputHTMLAttributes } from "react";
import "./Checkbox.css";

export type CheckboxState = "default" | "disabled";
export type CheckboxValueType = "checked" | "unchecked" | "indeterminate";

export interface CheckboxProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, "type" | "checked" | "disabled"> {
  state?: CheckboxState;
  valueType?: CheckboxValueType;
  label?: string;
  disabled?: boolean;
}

export function Checkbox({
  state = "default",
  valueType = "unchecked",
  label,
  disabled = false,
  className = "",
  ...rest
}: CheckboxProps) {
  const inputRef = useRef<HTMLInputElement>(null);
  const visualState: CheckboxState = disabled ? "disabled" : state;
  const checked = valueType === "checked";
  const indeterminate = valueType === "indeterminate";

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.indeterminate = indeterminate;
    }
  }, [indeterminate]);

  const wrapperClass = [
    "sds-checkbox",
    `sds-checkbox--${visualState}`,
    `sds-checkbox--${valueType}`,
    className
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <label className={wrapperClass}>
      <input
        ref={inputRef}
        className="sds-checkbox__input"
        type="checkbox"
        checked={checked}
        disabled={visualState === "disabled"}
        readOnly
        {...rest}
      />
      <span className="sds-checkbox__box" aria-hidden />
      {label ? <span className="sds-checkbox__label">{label}</span> : null}
    </label>
  );
}
