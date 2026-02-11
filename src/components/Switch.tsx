import type { InputHTMLAttributes } from "react";
import "./Switch.css";

export type SwitchState = "default" | "disabled";
export type SwitchValueType = "checked" | "unchecked";

export interface SwitchProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, "type" | "checked" | "disabled"> {
  state?: SwitchState;
  valueType?: SwitchValueType;
  label?: string;
  disabled?: boolean;
}

export function Switch({
  state = "default",
  valueType = "unchecked",
  label,
  disabled = false,
  className = "",
  ...rest
}: SwitchProps) {
  const visualState: SwitchState = disabled ? "disabled" : state;
  const checked = valueType === "checked";

  const wrapperClass = [
    "sds-switch",
    `sds-switch--${visualState}`,
    checked ? "sds-switch--checked" : "sds-switch--unchecked",
    className
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <label className={wrapperClass}>
      <input
        className="sds-switch__input"
        type="checkbox"
        checked={checked}
        disabled={visualState === "disabled"}
        readOnly
        {...rest}
      />
      <span className="sds-switch__track" aria-hidden>
        <span className="sds-switch__thumb" />
      </span>
      {label ? <span className="sds-switch__label">{label}</span> : null}
    </label>
  );
}
