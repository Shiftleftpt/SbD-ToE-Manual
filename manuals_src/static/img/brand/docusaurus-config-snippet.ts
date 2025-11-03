// Place inside themeConfig / root of docusaurus.config.ts
export default {
  // ...
  favicon: 'img/brand/favicon-32.png',
  themeConfig: {
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
      disableSwitch: false,
    },
    navbar: {
      title: 'SbD-ToE',
      logo: {
        alt: 'ShiftLeft · SbD-ToE',
        src: 'img/brand/Shiftleft_LogoHorizontal_V5.png',
        srcDark: 'img/brand/Shiftleft_LogoHorizontal_V5.png',
      },
    },
  },
};
