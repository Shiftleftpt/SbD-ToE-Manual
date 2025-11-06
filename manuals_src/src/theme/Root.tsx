// manuals_src/src/theme/Root.tsx
import React, {useEffect} from 'react';
import {useLocation} from '@docusaurus/router';

declare global {
  interface Window {
    plausible?: any;
  }
}

export default function Root({children}: {children: React.ReactNode}) {
  const location = useLocation();

  // Inicializa o wrapper, para o caso do bundle expor plausible.init()
  useEffect(() => {
    if (typeof window !== 'undefined') {
      window.plausible =
        window.plausible ||
        function () {
          (window.plausible.q = window.plausible.q || []).push(arguments);
        };
      if (typeof window.plausible.init === 'function') {
        window.plausible.init();
      }
    }
  }, []);

  // Dispara pageview a cada navegação interna (SPA)
  useEffect(() => {
    if (typeof window !== 'undefined' && typeof window.plausible === 'function') {
      window.plausible('pageview');
    }
  }, [location.pathname, location.search, location.hash]);

  return <>{children}</>;
}
