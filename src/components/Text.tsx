import type { ElementType, HTMLAttributes } from "react";
import "./Text.css";

export type TextVariant =
  | "body"
  | "strong"
  | "emphasis"
  | "link"
  | "small"
  | "code"
  | "heading"
  | "subheading"
  | "subtitle"
  | "titlePage"
  | "titleHero";

type IntrinsicTag = ElementType;

export interface TextProps extends HTMLAttributes<HTMLElement> {
  variant?: TextVariant;
  as?: IntrinsicTag;
}

export function Text({ variant = "body", as, className = "", children, ...rest }: TextProps) {
  const Tag = as ?? defaultTagByVariant[variant];
  const classes = ["sds-text", `sds-text--${variant}`, className].filter(Boolean).join(" ");

  return (
    <Tag className={classes} {...rest}>
      {children}
    </Tag>
  );
}

const defaultTagByVariant: Record<TextVariant, IntrinsicTag> = {
  body: "p",
  strong: "p",
  emphasis: "p",
  link: "a",
  small: "small",
  code: "code",
  heading: "h3",
  subheading: "h4",
  subtitle: "h2",
  titlePage: "h1",
  titleHero: "h1"
};
