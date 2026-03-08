svg = '''            <svg id="hero-svg" viewBox="0 0 560 530" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:auto">
              <defs>
                <linearGradient id="gc" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#e2e8f0"/><stop offset="100%" stop-color="#cbd5e1"/>
                </linearGradient>
                <linearGradient id="gblue" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="#2563eb"/><stop offset="100%" stop-color="#1d4ed8"/>
                </linearGradient>
                <linearGradient id="gnotif" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#eff6ff"/><stop offset="100%" stop-color="#ffffff"/>
                </linearGradient>
                <filter id="fs"><feDropShadow dx="1" dy="3" stdDeviation="6" flood-color="rgba(0,0,0,0.10)"/></filter>
                <filter id="fh"><feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="rgba(37,99,235,0.20)"/></filter>
                <filter id="fglow"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#2563eb" flood-opacity="0.45"/></filter>
                <filter id="fgreen"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#22c55e" flood-opacity="0.5"/></filter>
                <style>
                  /* ============================================================
                     HERO SVG — 20 s auto-play loop
                     0-25%  (0-5s)      GAMING
                     25-47% (5-9.4s)    NOTIFICATION
                     47-58% (9.4-11.6s) TRANSITION
                     58-96% (11.6-19.2s)CODING
                     96-100%            RESET
                     ============================================================ */
                  @keyframes aPhone     { 0%,28%{opacity:1;transform:translateY(0) scale(1)} 44%{opacity:0;transform:translateY(35px) scale(0.5)} 97%{opacity:0;transform:translateY(35px) scale(0.5)} 100%{opacity:1;transform:translateY(0) scale(1)} }
                  @keyframes aNotif     { 0%,24%{opacity:0;transform:translateX(200px) scale(1)} 32%{opacity:1;transform:translateX(0) scale(1)} 43%{opacity:1;transform:translateX(0) scale(1)} 49%{opacity:0;transform:translateX(-85px) translateY(22px) scale(0.06)} 100%{opacity:0;transform:translateX(200px) scale(1)} }
                  @keyframes aNotifGlow { 0%,24%{opacity:0} 32%{opacity:1} 43%{opacity:1} 49%{opacity:0} 100%{opacity:0} }
                  @keyframes aNotifPulse{ 0%,100%{transform:scale(1)} 50%{transform:scale(1.22)} }
                  @keyframes aGameScr   { 0%,30%{opacity:1} 42%{opacity:0} 97%{opacity:0} 100%{opacity:1} }
                  @keyframes aIdleScr   { 0%,44%{opacity:0} 48%,56%{opacity:1} 62%{opacity:0} 100%{opacity:0} }
                  @keyframes aCodeScr   { 0%,58%{opacity:0} 64%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aSmile     { 0%,30%{opacity:1} 38%{opacity:0} 97%{opacity:0} 100%{opacity:1} }
                  @keyframes aSurp      { 0%,36%{opacity:0} 40%,52%{opacity:1} 57%{opacity:0} 100%{opacity:0} }
                  @keyframes aFocus     { 0%,57%{opacity:0} 63%{opacity:1} 95%{opacity:1} 100%{opacity:0} }
                  @keyframes aPupil     { 0%,28%{transform:translate(0,4px)} 34%,46%{transform:translate(4px,-1px)} 55%,96%{transform:translate(0,-2px)} 100%{transform:translate(0,4px)} }
                  @keyframes aHead      { 0%,26%{transform:rotate(10deg)} 34%{transform:rotate(-6deg)} 52%{transform:rotate(0deg)} 58%,94%{transform:rotate(-4deg)} 100%{transform:rotate(10deg)} }
                  @keyframes aArmsGame  { 0%,30%{opacity:1} 45%{opacity:0} 97%{opacity:0} 100%{opacity:1} }
                  @keyframes aArmsCoding{ 0%,55%{opacity:0} 63%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aWASD      { 0%,28%{opacity:1} 38%{opacity:0} 97%{opacity:0} 100%{opacity:1} }
                  @keyframes aCodeKeys  { 0%,57%{opacity:0} 63%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCL1 { 0%,60%{opacity:0} 64%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCL2 { 0%,65%{opacity:0} 69%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCL3 { 0%,69%{opacity:0} 73%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCL4 { 0%,73%{opacity:0} 77%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCL5 { 0%,77%{opacity:0} 81%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCL6 { 0%,81%{opacity:0} 85%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCursorVis { 0%,59%{opacity:0} 64%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aCursorBlink { 0%,100%{opacity:1} 50%{opacity:0} }
                  @keyframes aLblGame  { 0%,27%{opacity:1} 32%{opacity:0} 97%{opacity:0} 100%{opacity:1} }
                  @keyframes aLblNotif { 0%,26%{opacity:0} 31%{opacity:1} 50%{opacity:1} 55%{opacity:0} 100%{opacity:0} }
                  @keyframes aLblCode  { 0%,60%{opacity:0} 65%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aGameChar { 0%,100%{transform:translateY(0)} 45%{transform:translateY(-12px)} }
                  @keyframes aEnemy    { 0%,100%{transform:translateX(0)} 50%{transform:translateX(-22px)} }
                  @keyframes aScoreUp  { 0%,60%{opacity:0;transform:translateY(0)} 65%{opacity:1;transform:translateY(-5px)} 90%{opacity:0;transform:translateY(-16px)} 100%{opacity:0;transform:translateY(0)} }
                  @keyframes aCoin     { 0%,100%{transform:translateY(0) scale(1)} 50%{transform:translateY(-4px) scale(1.15)} }
                  @keyframes aHeadphones { 0%,30%{opacity:1} 38%{opacity:0} 97%{opacity:0} 100%{opacity:1} }
                  @keyframes aExclaim  { 0%,36%{opacity:0;transform:scale(0.5)} 40%{opacity:1;transform:scale(1.2)} 44%{opacity:1;transform:scale(1)} 52%{opacity:1} 57%{opacity:0} 100%{opacity:0} }
                  @keyframes aMonGlow  { 0%,58%{opacity:0} 64%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }
                  @keyframes aScanLine { 0%{transform:translateY(0)} 100%{transform:translateY(82px)} }
                  @keyframes aStarBlink { 0%,100%{opacity:0.4} 50%{opacity:1} }
                  @keyframes aHealthBar { 0%,28%{width:32px} 25%{width:24px} 20%{width:30px} 15%{width:28px} }
                  @keyframes aTermLine { 0%,85%{opacity:0} 88%{opacity:1} 96%{opacity:1} 99%{opacity:0} 100%{opacity:0} }

                  #phone-grp      { animation: aPhone      20s ease-in-out infinite; }
                  #notif-grp      { animation: aNotif      20s cubic-bezier(.4,0,.2,1) infinite; transform-origin:330px 230px; }
                  #notif-glow-ring{ animation: aNotifGlow  20s ease-in-out infinite; }
                  #idle-scr       { animation: aIdleScr    20s ease-in-out infinite; }
                  #code-scr       { animation: aCodeScr    20s ease-in-out infinite; }
                  #arms-gaming    { animation: aArmsGame   20s ease-in-out infinite; }
                  #arms-coding    { animation: aArmsCoding 20s ease-in-out infinite; }
                  #wasd-keys      { animation: aWASD       20s infinite; }
                  #code-keys      { animation: aCodeKeys   20s infinite; }
                  #head-grp       { animation: aHead       20s ease-in-out infinite; transform-box:fill-box; transform-origin:50% 50%; }
                  #pupils         { animation: aPupil      20s ease-in-out infinite; transform-box:fill-box; transform-origin:50% 50%; }
                  #expr-smile     { animation: aSmile      20s ease-in-out infinite; }
                  #expr-surp      { animation: aSurp       20s ease-in-out infinite; }
                  #exclaim        { animation: aExclaim    20s ease-in-out infinite; transform-box:fill-box; transform-origin:50% 100%; }
                  #brow-surp      { animation: aSurp       20s ease-in-out infinite; }
                  #brow-surp2     { animation: aSurp       20s ease-in-out infinite; }
                  #expr-focus     { animation: aFocus      20s ease-in-out infinite; }
                  #game-screen-g  { animation: aGameScr    20s ease-in-out infinite; }
                  #headphones-g   { animation: aHeadphones 20s ease-in-out infinite; }
                  #cl1            { animation: aCL1        20s infinite; }
                  #cl2            { animation: aCL2        20s infinite; }
                  #cl3            { animation: aCL3        20s infinite; }
                  #cl4            { animation: aCL4        20s infinite; }
                  #cl5            { animation: aCL5        20s infinite; }
                  #cl6            { animation: aCL6        20s infinite; }
                  #term-line      { animation: aTermLine   20s infinite; }
                  #cursor-wrap    { animation: aCursorVis  20s infinite; }
                  #cursor-rect    { animation: aCursorBlink 0.75s ease-in-out infinite; }
                  #lbl-game       { animation: aLblGame    20s infinite; }
                  #lbl-notif      { animation: aLblNotif   20s infinite; opacity:0; }
                  #lbl-code       { animation: aLblCode    20s infinite; opacity:0; }
                  #notif-badge    { animation: aNotifPulse 0.6s ease-in-out infinite; transform-box:fill-box; transform-origin:50% 50%; }
                  #phone-hero     { animation: aGameChar   0.65s ease-in-out infinite; }
                  #phone-enemy    { animation: aEnemy      1.4s ease-in-out infinite; }
                  #game-coin      { animation: aCoin       0.9s ease-in-out infinite; }
                  #score-up       { animation: aScoreUp    20s ease-in-out infinite; }
                  #mon-glow       { animation: aMonGlow    20s ease-in-out infinite; }
                  #scan-line      { animation: aScanLine   2s linear infinite; }
                  .star1          { animation: aStarBlink  1.2s ease-in-out infinite; }
                  .star2          { animation: aStarBlink  1.8s ease-in-out infinite 0.4s; }
                  .star3          { animation: aStarBlink  1.5s ease-in-out infinite 0.8s; }
                </style>
              </defs>

              <!-- ===== DESK ===== -->
              <rect x="40" y="338" width="480" height="14" rx="7" fill="#e2e8f0" filter="url(#fs)"/>
              <rect x="78" y="352" width="14" height="75" rx="6" fill="#cbd5e1"/>
              <rect x="460" y="352" width="14" height="75" rx="6" fill="#cbd5e1"/>

              <!-- ===== MONITOR ===== -->
              <!-- monitor glow (coding only) -->
              <rect id="mon-glow" x="143" y="152" width="258" height="182" rx="14" fill="none" stroke="#2563eb" stroke-width="3" opacity="0" filter="url(#fglow)"/>
              <!-- frame -->
              <rect x="145" y="155" width="254" height="178" rx="12" fill="#1e293b" filter="url(#fh)"/>
              <rect x="155" y="164" width="234" height="162" rx="8" fill="#0f172a"/>
              <!-- stand -->
              <rect x="267" y="333" width="24" height="18" rx="5" fill="#475569"/>
              <rect x="245" y="350" width="68" height="9" rx="5" fill="#475569"/>

              <!-- IDLE SCREEN -->
              <g id="idle-scr">
                <rect x="155" y="164" width="234" height="162" rx="8" fill="#1e293b"/>
                <circle cx="272" cy="245" r="18" fill="#334155" opacity="0.6"/>
                <text x="272" y="250" font-family="Inter,sans-serif" font-size="13" fill="#475569" text-anchor="middle">⏸</text>
                <text x="272" y="268" font-family="Inter,sans-serif" font-size="8" fill="#334155" text-anchor="middle">STANDBY</text>
              </g>

              <!-- CODE SCREEN -->
              <g id="code-scr">
                <rect x="155" y="164" width="234" height="162" rx="8" fill="#0d1117"/>
                <!-- tab bar -->
                <rect x="155" y="164" width="234" height="18" rx="8" fill="#161b22"/>
                <rect x="155" y="174" width="234" height="8" fill="#161b22"/>
                <rect x="162" y="167" width="68" height="12" rx="3" fill="#0d1117"/>
                <text x="168" y="176" font-family="'Fira Code',monospace" font-size="6" fill="#58a6ff">⬤ </text>
                <text x="179" y="176" font-family="'Fira Code',monospace" font-size="6" fill="#8b949e">server.js</text>
                <!-- line numbers -->
                <g font-family="'Fira Code',monospace" font-size="7.5" fill="#3d444d">
                  <text x="160" y="196">1</text><text x="160" y="208">2</text>
                  <text x="160" y="220">3</text><text x="160" y="232">4</text>
                  <text x="160" y="244">5</text><text x="160" y="256">6</text>
                  <text x="160" y="268">7</text>
                </g>
                <!-- divider line -->
                <line x1="172" y1="184" x2="172" y2="326" stroke="#21262d" stroke-width="1"/>
                <!-- code content -->
                <text x="177" y="196" font-family="'Fira Code',monospace" font-size="7.5" fill="#8b949e">// backend/server.js</text>
                <text id="cl1" x="177" y="208" font-family="'Fira Code',monospace" font-size="7.5" fill="#ff7b72" opacity="0">const <tspan fill="#e6edf3">express = </tspan><tspan fill="#79c0ff">require</tspan><tspan fill="#e6edf3">(</tspan><tspan fill="#a5d6ff">'express'</tspan><tspan fill="#e6edf3">);</tspan></text>
                <text id="cl2" x="177" y="220" font-family="'Fira Code',monospace" font-size="7.5" fill="#ff7b72" opacity="0">const <tspan fill="#e6edf3">app = </tspan><tspan fill="#79c0ff">express</tspan><tspan fill="#e6edf3">();</tspan></text>
                <text id="cl3" x="177" y="232" font-family="'Fira Code',monospace" font-size="7.5" fill="#e6edf3" opacity="0">app.<tspan fill="#d2a8ff">get</tspan><tspan>('</tspan><tspan fill="#a5d6ff">/api</tspan><tspan>',(req,res)=&gt;{</tspan></text>
                <text id="cl4" x="185" y="244" font-family="'Fira Code',monospace" font-size="7.5" fill="#e6edf3" opacity="0">  res.<tspan fill="#d2a8ff">json</tspan><tspan>({</tspan><tspan fill="#79c0ff">ok</tspan><tspan>:</tspan><tspan fill="#56d364">true</tspan><tspan>});</tspan></text>
                <text id="cl5" x="177" y="256" font-family="'Fira Code',monospace" font-size="7.5" fill="#e6edf3" opacity="0">});</text>
                <text id="cl6" x="177" y="268" font-family="'Fira Code',monospace" font-size="7.5" fill="#56d364" opacity="0">app.<tspan fill="#d2a8ff">listen</tspan><tspan fill="#e6edf3">(</tspan><tspan fill="#79c0ff">3000</tspan><tspan fill="#e6edf3">);</tspan></text>
                <!-- terminal line -->
                <rect x="155" y="296" width="234" height="30" rx="0" fill="#010409"/>
                <rect x="155" y="296" width="234" height="1" fill="#21262d"/>
                <text x="160" y="308" font-family="'Fira Code',monospace" font-size="6.5" fill="#3fb950">$ </text><text id="term-line" x="170" y="308" font-family="'Fira Code',monospace" font-size="6.5" fill="#58a6ff" opacity="0">node server.js</text>
                <text x="160" y="320" font-family="'Fira Code',monospace" font-size="6.5" fill="#3fb950" opacity="0" id="term-line">✓ Server running on :3000</text>
                <!-- cursor -->
                <g id="cursor-wrap">
                  <rect id="cursor-rect" x="177" y="274" width="6" height="10" rx="1" fill="#58a6ff"/>
                </g>
              </g>

              <!-- ===== CHAIR BACK ===== -->
              <rect x="192" y="300" width="174" height="88" rx="16" fill="url(#gc)" filter="url(#fs)"/>
              <rect x="148" y="342" width="24" height="50" rx="10" fill="#cbd5e1"/>
              <rect x="386" y="342" width="24" height="50" rx="10" fill="#cbd5e1"/>
              <rect x="212" y="280" width="134" height="30" rx="12" fill="#d1d5db"/>

              <!-- ===== BODY ===== -->
              <rect x="235" y="302" width="88" height="80" rx="14" fill="#3b82f6"/>
              <rect x="264" y="304" width="12" height="42" rx="5" fill="#2563eb"/>
              <!-- collar -->
              <path d="M262 305 L280 305 L272 318 Z" fill="#eff6ff" opacity="0.4"/>
              <!-- neck -->
              <rect x="258" y="288" width="28" height="22" rx="8" fill="#fbbf24"/>

              <!-- ===== ARMS (GAMING) ===== -->
              <g id="arms-gaming">
                <rect x="178" y="325" width="60" height="18" rx="9" fill="#fbbf24" transform="rotate(38,205,325)"/>
                <ellipse cx="202" cy="360" rx="14" ry="12" fill="#fbbf24"/>
                <rect x="318" y="325" width="60" height="18" rx="9" fill="#fbbf24" transform="rotate(-38,350,325)"/>
                <ellipse cx="358" cy="360" rx="14" ry="12" fill="#fbbf24"/>
              </g>

              <!-- ===== ARMS (CODING) ===== -->
              <g id="arms-coding">
                <rect x="165" y="322" width="72" height="16" rx="9" fill="#fbbf24" transform="rotate(12,200,330)"/>
                <ellipse cx="188" cy="344" rx="14" ry="12" fill="#fbbf24"/>
                <rect x="320" y="322" width="72" height="16" rx="9" fill="#fbbf24" transform="rotate(-12,357,330)"/>
                <ellipse cx="370" cy="344" rx="14" ry="12" fill="#fbbf24"/>
              </g>

              <!-- ===== PHONE GROUP ===== -->
              <g id="phone-grp">
                <rect x="242" y="298" width="74" height="118" rx="12" fill="#1e293b" filter="url(#fs)"/>
                <rect x="265" y="301" width="28" height="6" rx="3" fill="#0f172a"/>
                <circle cx="267" cy="304" r="2" fill="#475569"/>
                <!-- GAME SCREEN (big) -->
                <g id="game-screen-g">
                  <rect x="246" y="310" width="66" height="98" rx="8" fill="#0c1445"/>
                  <!-- sky gradient band -->
                  <rect x="246" y="310" width="66" height="50" rx="8" fill="#1a237e" opacity="0.8"/>
                  <!-- stars -->
                  <circle class="star1" cx="252" cy="316" r="1.2" fill="#fff"/>
                  <circle class="star2" cx="263" cy="313" r="1" fill="#fff"/>
                  <circle class="star3" cx="275" cy="318" r="1.3" fill="#fff"/>
                  <circle class="star1" cx="288" cy="314" r="1" fill="#fff"/>
                  <circle class="star2" cx="300" cy="317" r="1.2" fill="#fff"/>
                  <circle class="star3" cx="255" cy="325" r="0.8" fill="#fff" opacity="0.6"/>
                  <!-- mountains -->
                  <polygon points="246,355 262,330 278,355" fill="#1a3a6b"/>
                  <polygon points="264,355 282,325 300,355" fill="#154360"/>
                  <!-- ground -->
                  <rect x="246" y="387" width="66" height="21" fill="#2e7d32"/>
                  <rect x="246" y="385" width="66" height="6" fill="#388e3c"/>
                  <!-- platforms -->
                  <rect x="252" y="375" width="22" height="5" rx="2" fill="#8b6914"/>
                  <rect x="282" y="365" width="20" height="5" rx="2" fill="#8b6914"/>
                  <!-- score bar -->
                  <rect x="246" y="310" width="66" height="13" rx="5" fill="#000" opacity="0.4"/>
                  <text x="249" y="320" font-family="monospace" font-size="6" fill="#ffd700">★2850</text>
                  <!-- health -->
                  <rect x="285" y="313" width="24" height="5" rx="2" fill="#b71c1c"/>
                  <rect x="285" y="313" width="18" height="5" rx="2" fill="#ef5350"/>
                  <text x="284" y="319" font-family="monospace" font-size="4.5" fill="#fff">♥</text>
                  <!-- HERO character -->
                  <g id="phone-hero">
                    <rect x="256" y="366" width="12" height="16" rx="3" fill="#ff9800"/>
                    <circle cx="262" cy="363" r="7" fill="#fbbf24"/>
                    <rect x="257" y="356" width="10" height="5" rx="2" fill="#d32f2f"/>
                    <circle cx="260" cy="362" r="2" fill="#fff"/><circle cx="265" cy="362" r="2" fill="#fff"/>
                    <circle cx="260" cy="362.8" r="1" fill="#1a1a1a"/><circle cx="265" cy="362.8" r="1" fill="#1a1a1a"/>
                    <path d="M259 367 Q262 369 265 367" fill="none" stroke="#92400e" stroke-width="1" stroke-linecap="round"/>
                    <!-- sword/weapon -->
                    <rect x="268" y="360" width="2" height="12" rx="1" fill="#90caf9"/>
                    <rect x="265" y="363" width="8" height="2" rx="1" fill="#90caf9"/>
                  </g>
                  <!-- ENEMY -->
                  <g id="phone-enemy">
                    <rect x="291" y="358" width="11" height="14" rx="3" fill="#7b1fa2"/>
                    <circle cx="296" cy="355" r="6" fill="#ab47bc"/>
                    <circle cx="293" cy="354" r="1.5" fill="#e0e0e0"/><circle cx="299" cy="354" r="1.5" fill="#e0e0e0"/>
                    <circle cx="293" cy="354.5" r="0.8" fill="#c62828"/><circle cx="299" cy="354.5" r="0.8" fill="#c62828"/>
                  </g>
                  <!-- COIN -->
                  <g id="game-coin">
                    <circle cx="278" cy="360" r="5" fill="#fdd835" stroke="#f9a825" stroke-width="1"/>
                    <text x="276" y="363" font-family="monospace" font-size="5" fill="#f57f17">$</text>
                  </g>
                  <!-- floating +100 score -->
                  <text id="score-up" x="272" y="382" font-family="monospace" font-size="7" fill="#ffd700" text-anchor="middle" opacity="0">+150 ★</text>
                  <!-- scan line effect -->
                  <rect id="scan-line" x="246" y="310" width="66" height="3" fill="#fff" opacity="0.04"/>
                </g>
              </g>

              <!-- ===== KEYBOARD ===== -->
              <rect x="162" y="330" width="234" height="50" rx="8" fill="#e2e8f0" filter="url(#fs)"/>
              <rect x="162" y="330" width="234" height="8" rx="4" fill="#d1d5db"/>
              <g fill="#c8d1dc">
                <rect x="172" y="341" width="14" height="10" rx="3"/><rect x="189" y="341" width="14" height="10" rx="3"/>
                <rect x="206" y="341" width="14" height="10" rx="3"/><rect x="223" y="341" width="14" height="10" rx="3"/>
                <rect x="240" y="341" width="14" height="10" rx="3"/><rect x="257" y="341" width="14" height="10" rx="3"/>
                <rect x="274" y="341" width="14" height="10" rx="3"/><rect x="291" y="341" width="14" height="10" rx="3"/>
                <rect x="308" y="341" width="14" height="10" rx="3"/><rect x="325" y="341" width="14" height="10" rx="3"/>
                <rect x="172" y="354" width="22" height="9" rx="3"/><rect x="197" y="354" width="14" height="9" rx="3"/>
                <rect x="214" y="354" width="14" height="9" rx="3"/><rect x="231" y="354" width="14" height="9" rx="3"/>
                <rect x="248" y="354" width="14" height="9" rx="3"/><rect x="265" y="354" width="14" height="9" rx="3"/>
                <rect x="282" y="354" width="14" height="9" rx="3"/><rect x="299" y="354" width="14" height="9" rx="3"/>
                <rect x="316" y="354" width="24" height="9" rx="3"/>
                <rect x="194" y="366" width="170" height="9" rx="3"/>
              </g>
              <!-- WASD gaming keys -->
              <g id="wasd-keys">
                <rect x="206" y="341" width="14" height="10" rx="3" fill="#2563eb" opacity="0.9"/>
                <text x="213" y="349" font-family="monospace" font-size="6" fill="#fff" text-anchor="middle">W</text>
                <rect x="197" y="354" width="14" height="9" rx="3" fill="#2563eb" opacity="0.9"/>
                <text x="204" y="361" font-family="monospace" font-size="6" fill="#fff" text-anchor="middle">A</text>
                <rect x="214" y="354" width="14" height="9" rx="3" fill="#2563eb" opacity="0.9"/>
                <text x="221" y="361" font-family="monospace" font-size="6" fill="#fff" text-anchor="middle">S</text>
                <rect x="231" y="354" width="14" height="9" rx="3" fill="#2563eb" opacity="0.9"/>
                <text x="238" y="361" font-family="monospace" font-size="6" fill="#fff" text-anchor="middle">D</text>
                <rect x="240" y="341" width="14" height="10" rx="3" fill="#1d4ed8" opacity="0.8"/>
                <text x="247" y="349" font-family="monospace" font-size="6" fill="#93c5fd" text-anchor="middle">↑</text>
              </g>
              <!-- Code keys (coding phase) -->
              <g id="code-keys">
                <rect x="274" y="341" width="14" height="10" rx="3" fill="#16a34a" opacity="0.9"/>
                <text x="281" y="349" font-family="monospace" font-size="6" fill="#fff" text-anchor="middle">{</text>
                <rect x="291" y="341" width="14" height="10" rx="3" fill="#16a34a" opacity="0.9"/>
                <text x="298" y="349" font-family="monospace" font-size="6" fill="#fff" text-anchor="middle">}</text>
                <rect x="194" y="366" width="170" height="9" rx="3" fill="#2563eb" opacity="0.65"/>
                <text x="280" y="373" font-family="monospace" font-size="5.5" fill="#fff" text-anchor="middle">SPACE</text>
              </g>

              <!-- ===== HEAD GROUP ===== -->
              <g id="head-grp" style="transform-box:fill-box;transform-origin:50% 50%">
                <!-- ears -->
                <ellipse cx="220" cy="262" rx="10" ry="13" fill="#f0a832"/>
                <ellipse cx="220" cy="262" rx="6" ry="8" fill="#e8921e" opacity="0.5"/>
                <ellipse cx="338" cy="262" rx="10" ry="13" fill="#f0a832"/>
                <ellipse cx="338" cy="262" rx="6" ry="8" fill="#e8921e" opacity="0.5"/>
                <!-- head -->
                <ellipse cx="279" cy="258" rx="52" ry="50" fill="#fbbf24"/>
                <!-- hair -->
                <ellipse cx="279" cy="218" rx="52" ry="20" fill="#1c1917"/>
                <rect x="227" y="217" width="104" height="26" rx="5" fill="#1c1917"/>
                <!-- glasses -->
                <rect x="244" y="255" width="26" height="16" rx="5" fill="none" stroke="#1c1917" stroke-width="3"/>
                <rect x="276" y="255" width="26" height="16" rx="5" fill="none" stroke="#1c1917" stroke-width="3"/>
                <line x1="270" y1="263" x2="276" y2="263" stroke="#1c1917" stroke-width="2.5"/>
                <line x1="220" y1="263" x2="244" y2="263" stroke="#1c1917" stroke-width="2.5"/>
                <line x1="302" y1="263" x2="325" y2="263" stroke="#1c1917" stroke-width="2.5"/>
                <!-- eyes -->
                <ellipse cx="257" cy="264" rx="9" ry="6" fill="#fff"/>
                <ellipse cx="289" cy="264" rx="9" ry="6" fill="#fff"/>
                <!-- pupils -->
                <g id="pupils" style="transform-box:fill-box;transform-origin:50% 50%">
                  <circle cx="257" cy="264" r="4.5" fill="#1e1e2e"/>
                  <circle cx="289" cy="264" r="4.5" fill="#1e1e2e"/>
                  <circle cx="258.5" cy="262.5" r="1.5" fill="#fff"/>
                  <circle cx="290.5" cy="262.5" r="1.5" fill="#fff"/>
                </g>
                <!-- SMILE -->
                <path id="expr-smile" d="M260 278 Q279 293 298 278" fill="none" stroke="#92400e" stroke-width="2.5" stroke-linecap="round"/>
                <!-- SURPRISED -->
                <ellipse id="expr-surp" cx="279" cy="281" rx="10" ry="8" fill="#92400e" opacity="0"/>
                <!-- FOCUSED -->
                <path id="expr-focus" d="M264 279 Q279 275 294 279" fill="none" stroke="#92400e" stroke-width="2.2" stroke-linecap="round" opacity="0"/>
                <!-- EYEBROWS gaming: calm -->
                <!-- EYEBROWS surprised -->
                <path id="brow-surp"  d="M244 248 Q257 241 270 247" fill="none" stroke="#1c1917" stroke-width="2.5" stroke-linecap="round" opacity="0"/>
                <path id="brow-surp2" d="M286 247 Q299 241 312 248" fill="none" stroke="#1c1917" stroke-width="2.5" stroke-linecap="round" opacity="0"/>
                <!-- EXCLAMATION mark above head -->
                <g id="exclaim" opacity="0">
                  <circle cx="279" cy="204" r="12" fill="#ef4444" opacity="0.9"/>
                  <text x="279" y="209" font-family="sans-serif" font-size="14" fill="#fff" text-anchor="middle" font-weight="bold">!</text>
                </g>
                <!-- HEADPHONES (gaming) -->
                <g id="headphones-g">
                  <path d="M226 256 Q226 216 279 216 Q332 216 332 256" fill="none" stroke="#374151" stroke-width="8" stroke-linecap="round"/>
                  <rect x="218" y="252" width="14" height="22" rx="7" fill="#374151"/>
                  <rect x="326" y="252" width="14" height="22" rx="7" fill="#374151"/>
                  <rect x="220" y="254" width="10" height="18" rx="5" fill="#2563eb" opacity="0.6"/>
                  <rect x="328" y="254" width="10" height="18" rx="5" fill="#2563eb" opacity="0.6"/>
                </g>
              </g>

              <!-- ===== NOTIFICATION ===== -->
              <g id="notif-grp" style="transform-origin:330px 230px">
                <!-- glow ring -->
                <circle id="notif-glow-ring" cx="387" cy="218" r="36" fill="none" stroke="#2563eb" stroke-width="2" opacity="0.3" filter="url(#fglow)"/>
                <!-- card background shadow -->
                <rect x="320" y="210" width="160" height="74" rx="14" fill="#1e293b" opacity="0.15" transform="translate(2,4)"/>
                <!-- card -->
                <rect x="318" y="208" width="160" height="74" rx="14" fill="url(#gnotif)" filter="url(#fs)"/>
                <!-- left accent bar -->
                <rect x="318" y="208" width="6" height="74" rx="4" fill="url(#gblue)"/>
                <!-- icon bg -->
                <circle cx="342" cy="232" r="14" fill="#dbeafe"/>
                <text x="342" y="237" font-family="serif" font-size="14" text-anchor="middle">💼</text>
                <!-- content -->
                <text x="362" y="224" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#0f172a">Job Alert!</text>
                <text x="362" y="236" font-family="Inter,sans-serif" font-size="7.5" fill="#374151">Backend Engineer</text>
                <text x="362" y="247" font-family="Inter,sans-serif" font-size="7" fill="#6b7280">Remote · Full-time</text>
                <text x="362" y="257" font-family="Inter,sans-serif" font-size="7" fill="#2563eb" font-weight="600">Apply now →</text>
                <!-- badge -->
                <g id="notif-badge" style="transform-box:fill-box;transform-origin:50% 50%">
                  <circle cx="468" cy="215" r="10" fill="#ef4444"/>
                  <text x="468" y="219" font-family="monospace" font-size="8" fill="#fff" text-anchor="middle" font-weight="bold">1</text>
                </g>
              </g>

              <!-- ===== CHAIR SEAT + BASE ===== -->
              <rect x="168" y="378" width="222" height="32" rx="14" fill="url(#gc)" filter="url(#fs)"/>
              <rect x="265" y="410" width="32" height="42" rx="7" fill="#94a3b8"/>
              <ellipse cx="281" cy="456" rx="64" ry="11" fill="#cbd5e1"/>
              <circle cx="228" cy="456" r="10" fill="#94a3b8"/>
              <circle cx="281" cy="462" r="10" fill="#94a3b8"/>
              <circle cx="332" cy="456" r="10" fill="#94a3b8"/>

              <!-- ===== COFFEE CUP ===== -->
              <g transform="translate(60,275)">
                <rect x="0" y="0" width="34" height="36" rx="5" fill="#fff" stroke="#e2e8f0" stroke-width="2"/>
                <rect x="0" y="0" width="34" height="13" rx="5" fill="#2563eb"/>
                <text x="17" y="10" font-family="monospace" font-size="8" fill="#fff" text-anchor="middle">☕</text>
                <path d="M34 12 Q44 12 44 21 Q44 30 34 30" fill="none" stroke="#e2e8f0" stroke-width="2"/>
                <path d="M9 -5 Q11 -12 9 -18" fill="none" stroke="#94a3b8" stroke-width="2" stroke-linecap="round" opacity="0.7">
                  <animate attributeName="d" values="M9 -5 Q11 -12 9 -18;M9 -5 Q7 -12 9 -18;M9 -5 Q11 -12 9 -18" dur="2s" repeatCount="indefinite"/>
                </path>
                <path d="M17 -5 Q19 -14 17 -20" fill="none" stroke="#94a3b8" stroke-width="2" stroke-linecap="round" opacity="0.7">
                  <animate attributeName="d" values="M17 -5 Q19 -14 17 -20;M17 -5 Q15 -14 17 -20;M17 -5 Q19 -14 17 -20" dur="2.4s" repeatCount="indefinite"/>
                </path>
                <path d="M25 -5 Q27 -11 25 -17" fill="none" stroke="#94a3b8" stroke-width="2" stroke-linecap="round" opacity="0.7">
                  <animate attributeName="d" values="M25 -5 Q27 -11 25 -17;M25 -5 Q23 -11 25 -17;M25 -5 Q27 -11 25 -17" dur="1.8s" repeatCount="indefinite"/>
                </path>
              </g>

              <!-- ===== STATUS LABELS ===== -->
              <g font-family="Inter,sans-serif" font-size="10.5" text-anchor="middle" font-weight="600">
                <rect x="162" y="464" width="256" height="24" rx="12" fill="#eff6ff" opacity="0"/>
                <text id="lbl-game"  x="280" y="480" fill="#2563eb">🎮 Playing Mobile Game...</text>
                <text id="lbl-notif" x="280" y="480" fill="#dc2626">💼 Job Alert received!</text>
                <text id="lbl-code"  x="280" y="480" fill="#16a34a">💻 Now Coding...</text>
              </g>
            </svg>'''

with open('/Users/acadify/Documents/priyanshu/index.html', 'r') as f:
    content = f.read()

# Find the svg start and end
svg_start = content.find('            <svg id="hero-svg"')
# Find the matching </svg> — walk forward and count depth
depth = 0
i = svg_start
while i < len(content):
    if content[i:i+4] == '<svg':
        depth += 1
    elif content[i:i+6] == '</svg>':
        depth -= 1
        if depth == 0:
            svg_end = i + 6
            break
    i += 1

print(f"SVG found: chars {svg_start} to {svg_end}")
new_content = content[:svg_start] + svg + content[svg_end:]
with open('/Users/acadify/Documents/priyanshu/index.html', 'w') as f:
    f.write(new_content)
print("Done! Lines:", new_content.count('\n'))
