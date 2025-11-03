// src/theme/Admonition/Types.js
import React from 'react';
import DefaultAdmonitionTypes from '@theme-original/Admonition/Types';

function UserStoryAdmonition(props) {
  // props: {title?: string, children: ReactNode}
  const {title, children} = props;
  return (
    <div
      className="sl-userstory"
      role="note"
      aria-label={title || 'User Story'}
      style={{
        borderRadius: 12,
        padding: '0.85rem 1rem',
        border: '1px solid var(--sl-us-br)',
        background: 'var(--sl-us-bg)',
        color: 'var(--sl-us-fg)',
        boxShadow: '0 6px 16px rgba(0,0,0,.06)',
      }}
    >
      <div style={{display:'flex', alignItems:'center', gap:'.5rem', fontWeight:700}}>
        <span aria-hidden="true" style={{fontSize:'1.1em'}}>📝</span>
        <span>{title || 'User Story'}</span>
      </div>
      <div style={{paddingTop:'.35rem'}}>
        {children}
      </div>
    </div>
  );
}

const AdmonitionTypes = {
  ...DefaultAdmonitionTypes,
  // adiciona (ou substitui) tipos aqui
  userstory: UserStoryAdmonition,
};

export default AdmonitionTypes;
