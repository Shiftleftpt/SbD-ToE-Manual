// src/components/Badge.tsx
import React from 'react';

type BadgeProps = {
  children: React.ReactNode;
  color?: 'info' | 'success' | 'warning' | 'danger';
};

const colorMap: Record<string, string> = {
  info: '#017BFF',
  success: '#28a745',
  warning: '#ffc107',
  danger: '#dc3545',
};

export default function Badge({ children, color = 'info' }: BadgeProps) {
  return (
    <span
      style={{
        backgroundColor: colorMap[color],
        color: 'white',
        padding: '0.2rem 0.6rem',
        borderRadius: '0.5rem',
        fontSize: '0.8rem',
        fontWeight: 600,
        display: 'inline-block',
        whiteSpace: 'nowrap',
      }}
    >
      {children}
    </span>
  );
}
