import type { ButtonHTMLAttributes } from "react";
import "./Button.css";

export type ButtonVariant = "primary" | "neutral" | "subtle";
export type ButtonTone = "default" | "danger";
export type ButtonSize = "small" | "medium";
export type ButtonVisualState = "default" | "hover" | "disabled";

export interface ButtonProps
  extends Omit<ButtonHTMLAttributes<HTMLButtonElement>, "disabled"> {
  variant?: ButtonVariant;
  tone?: ButtonTone;
  size?: ButtonSize;
  state?: ButtonVisualState;
  disabled?: boolean;
}

export function Button({
  variant = "primary",
  tone = "default",
  size = "medium",
  state = "default",
  disabled = false,
  className = "",
  children,
  ...rest
}: ButtonProps) {
  const visualState: ButtonVisualState = disabled ? "disabled" : state;
  const classes = [
    "sds-button",
    `sds-button--${tone}`,
    `sds-button--${variant}`,
    `sds-button--${size}`,
    `sds-button--${visualState}`,
    className
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <button className={classes} disabled={disabled || visualState === "disabled"} {...rest}>
      {children}
    </button>
  );
}
