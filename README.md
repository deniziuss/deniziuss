<svg width="1200" height="340" viewBox="0 0 1200 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="340" gradientUnits="userSpaceOnUse">
      <stop stop-color="#070B12"/>
      <stop offset="1" stop-color="#0B1220"/>
    </linearGradient>

    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#22D3EE"/>
      <stop offset="1" stop-color="#8B5CF6"/>
    </linearGradient>

    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#1E293B" stroke-width="1" opacity="0.22"/>
    </pattern>

    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect x="1" y="1" width="1198" height="338" rx="20" fill="url(#bg)" stroke="#1E293B" stroke-width="2"/>
  <rect x="1" y="1" width="1198" height="338" rx="20" fill="url(#grid)"/>

  <!-- Top micro-labels -->
  <text x="48" y="46"
        fill="#22D3EE"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="13"
        font-weight="600"
        letter-spacing="2">
    DENIZ / SYSTEMS
  </text>

  <text x="1028" y="46"
        fill="#64748B"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12"
        letter-spacing="1.5">
    SYSTEM // 001
  </text>

  <!-- Left section -->
  <text x="48" y="118"
        fill="#F8FAFC"
        font-family="Inter, Arial, sans-serif"
        font-size="48"
        font-weight="700">
    Deniz Fersiz
  </text>

  <text x="48" y="158"
        fill="#CBD5E1"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="18">
    Software Development · Cybersecurity · AI &amp; Automation
  </text>

  <text x="48" y="207"
        fill="#64748B"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="15">
    Python · C# · C++ · Linux · Networking
  </text>

  <!-- Divider -->
  <line x1="620" y1="78" x2="620" y2="270" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Right section -->
  <text x="666" y="92"
        fill="#94A3B8"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12"
        letter-spacing="2">
    CURRENT FOCUS
  </text>

  <g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="14">
    <text x="666" y="128" fill="#64748B">01</text>
    <text x="706" y="128" fill="#E2E8F0">SOFTWARE</text>
    <circle cx="1004" cy="123" r="4" fill="#22D3EE" filter="url(#softGlow)"/>

    <text x="666" y="160" fill="#64748B">02</text>
    <text x="706" y="160" fill="#E2E8F0">SECURITY</text>
    <circle cx="1004" cy="155" r="4" fill="#22D3EE"/>

    <text x="666" y="192" fill="#64748B">03</text>
    <text x="706" y="192" fill="#E2E8F0">AI SYSTEMS</text>
    <circle cx="1004" cy="187" r="4" fill="#8B5CF6"/>

    <text x="666" y="224" fill="#64748B">04</text>
    <text x="706" y="224" fill="#E2E8F0">AUTOMATION</text>
    <circle cx="1004" cy="219" r="4" fill="#22D3EE"/>

    <text x="666" y="256" fill="#64748B">05</text>
    <text x="706" y="256" fill="#E2E8F0">NETWORKING</text>
    <circle cx="1004" cy="251" r="4" fill="#8B5CF6"/>
  </g>

  <!-- Node motif -->
  <g opacity="0.35">
    <line x1="1080" y1="120" x2="1120" y2="165" stroke="url(#accent)" stroke-width="1.5"/>
    <line x1="1120" y1="165" x2="1094" y2="218" stroke="url(#accent)" stroke-width="1.5"/>
    <line x1="1120" y1="165" x2="1160" y2="202" stroke="url(#accent)" stroke-width="1.5"/>

    <circle cx="1080" cy="120" r="5" fill="#22D3EE"/>
    <circle cx="1120" cy="165" r="6" fill="#8B5CF6"/>
    <circle cx="1094" cy="218" r="5" fill="#22D3EE"/>
    <circle cx="1160" cy="202" r="5" fill="#8B5CF6"/>
  </g>

  <!-- Bottom signature line -->
  <line x1="48" y1="292" x2="1152" y2="292" stroke="#1E293B" stroke-width="1"/>

  <text x="48" y="316"
        fill="#475569"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12"
        letter-spacing="2">
    BUILD
  </text>

  <text x="145" y="316"
        fill="#334155"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12">
    ─────────────
  </text>

  <text x="284" y="316"
        fill="#475569"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12"
        letter-spacing="2">
    ANALYZE
  </text>

  <text x="405" y="316"
        fill="#334155"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12">
    ─────────────
  </text>

  <text x="545" y="316"
        fill="#475569"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12"
        letter-spacing="2">
    AUTOMATE
  </text>

  <text x="1041" y="316"
        fill="#22D3EE"
        font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
        font-size="12"
        letter-spacing="1">
    STATUS: BUILDING
  </text>
</svg>
