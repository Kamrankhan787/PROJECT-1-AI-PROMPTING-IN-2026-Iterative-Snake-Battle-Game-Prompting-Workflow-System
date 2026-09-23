/**
 * SNAKE BATTLE — AI Prompting in 2026 Core Game Engine
 * Featuring: Multi-AI Opponents, Rule 5 Corpse-to-Fruit Conversion,
 * Web Audio Synthesizer, Touch Controls, Particle Engine & Full HUD.
 */

(function () {
  'use strict';

  // --- Grid & Arena Constants ---
  const GRID_SIZE = 30; // 30x30 cells
  const BASE_CANVAS_SIZE = 600;
  const CELL_SIZE = BASE_CANVAS_SIZE / GRID_SIZE; // 20px

  // Speed tick settings in milliseconds
  const SPEED_CONFIG = {
    Easy: 140,
    Normal: 105,
    Fast: 75,
    Frenzy: 48
  };

  // AI Configurations
  const AI_PRESETS = [
    { id: 'ai_1', name: 'Cyber Viper', color: '#ff4444', behavior: 'Aggressive', startX: 24, startY: 5, dir: { x: -1, y: 0 } },
    { id: 'ai_2', name: 'Neon Cobra', color: '#00d4ff', behavior: 'Balanced', startX: 24, startY: 24, dir: { x: 0, y: -1 } },
    { id: 'ai_3', name: 'Ghost Python', color: '#e056fd', behavior: 'Cautious', startX: 5, startY: 5, dir: { x: 0, y: 1 } },
    { id: 'ai_4', name: 'Solar Basilisk', color: '#ffbe76', behavior: 'Balanced', startX: 15, startY: 4, dir: { x: 1, y: 0 } }
  ];

  // --- Sound Synthesizer (Web Audio API) ---
  class SoundFX {
    constructor() {
      this.enabled = true;
      this.ctx = null;
    }

    init() {
      if (!this.ctx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) {
          this.ctx = new AudioContext();
        }
      }
      if (this.ctx && this.ctx.state === 'suspended') {
        this.ctx.resume();
      }
    }

    toggle() {
      this.enabled = !this.enabled;
      return this.enabled;
    }

    playEat() {
      if (!this.enabled) return;
      this.init();
      if (!this.ctx) return;

      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      const now = this.ctx.currentTime;

      osc.type = 'triangle';
      osc.frequency.setValueAtTime(440, now);
      osc.frequency.exponentialRampToValueAtTime(880, now + 0.1);

      gain.gain.setValueAtTime(0.18, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.1);
    }

    playDeath() {
      if (!this.enabled) return;
      this.init();
      if (!this.ctx) return;

      const now = this.ctx.currentTime;
      // White noise explosion burst
      const bufferSize = this.ctx.sampleRate * 0.25;
      const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
      const output = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        output[i] = Math.random() * 2 - 1;
      }

      const whiteNoise = this.ctx.createBufferSource();
      whiteNoise.buffer = buffer;

      const filter = this.ctx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(800, now);
      filter.frequency.linearRampToValueAtTime(80, now + 0.25);

      const gain = this.ctx.createGain();
      gain.gain.setValueAtTime(0.3, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);

      whiteNoise.connect(filter);
      filter.connect(gain);
      gain.connect(this.ctx.destination);

      whiteNoise.start(now);
    }

    playClick() {
      if (!this.enabled) return;
      this.init();
      if (!this.ctx) return;

      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      const now = this.ctx.currentTime;

      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, now);
      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now);
      osc.stop(now + 0.05);
    }

    playVictory() {
      if (!this.enabled) return;
      this.init();
      if (!this.ctx) return;

      const now = this.ctx.currentTime;
      const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
      notes.forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        const start = now + idx * 0.09;

        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, start);

        gain.gain.setValueAtTime(0.2, start);
        gain.gain.exponentialRampToValueAtTime(0.01, start + 0.15);

        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(start);
        osc.stop(start + 0.16);
      });
    }
  }

  // --- Particle FX Engine ---
  class ParticleEngine {
    constructor() {
      this.particles = [];
    }

    emit(x, y, color, count = 12, speedMultiplier = 1) {
      for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = (Math.random() * 3 + 1.5) * speedMultiplier;
        this.particles.push({
          x: x * CELL_SIZE + CELL_SIZE / 2,
          y: y * CELL_SIZE + CELL_SIZE / 2,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed,
          color: color,
          size: Math.random() * 4 + 2,
          alpha: 1.0,
          decay: Math.random() * 0.03 + 0.02
        });
      }
    }

    update() {
      for (let i = this.particles.length - 1; i >= 0; i--) {
        const p = this.particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.alpha -= p.decay;
        if (p.alpha <= 0) {
          this.particles.splice(i, 1);
        }
      }
    }

    draw(ctx) {
      ctx.save();
      for (const p of this.particles) {
        ctx.globalAlpha = Math.max(0, p.alpha);
        ctx.fillStyle = p.color;
        ctx.shadowColor = p.color;
        ctx.shadowBlur = 6;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    }
  }

  // --- Main Snake Class ---
  class Snake {
    constructor(id, name, color, initialPositions, dir, isAI = false) {
      this.id = id;
      this.name = name;
      this.color = color;
      this.segments = initialPositions.map(p => ({ ...p }));
      this.dir = { ...dir };
      this.nextDir = { ...dir };
      this.isAlive = true;
      this.isAI = isAI;
      this.pendingGrowth = 0;
      this.fruitsEaten = 0;
      this.kills = 0;
    }

    get head() {
      return this.segments[0];
    }

    get body() {
      return this.segments.slice(1);
    }

    get length() {
      return this.segments.length;
    }

    setDirection(newDir) {
      // Prevent reversing directly into itself
      if (this.dir.x + newDir.x === 0 && this.dir.y + newDir.y === 0) {
        return false;
      }
      this.nextDir = { ...newDir };
      return true;
    }

    grow(amount = 1) {
      this.pendingGrowth += amount;
      this.fruitsEaten += 1;
    }

    move() {
      if (!this.isAlive) return;

      this.dir = { ...this.nextDir };
      const newHead = {
        x: this.head.x + this.dir.x,
        y: this.head.y + this.dir.y
      };

      this.segments.unshift(newHead);

      if (this.pendingGrowth > 0) {
        this.pendingGrowth -= 1;
      } else {
        this.segments.pop();
      }
    }

    die() {
      this.isAlive = false;
    }

    /**
     * Rule 5: When a snake dies, its body segments convert into fruit
     * so other snakes can eat them.
     */
    convertToFruits() {
      const converted = this.segments.map(s => ({ ...s }));
      this.segments = [];
      return converted;
    }
  }

  // --- Game Engine Controller ---
  class SnakeBattleEngine {
    constructor() {
      this.canvas = document.getElementById('game-canvas');
      this.ctx = this.canvas.getContext('2d');
      this.sound = new SoundFX();
      this.particles = new ParticleEngine();

      // UI References
      this.startScreen = document.getElementById('start-screen');
      this.pauseScreen = document.getElementById('pause-screen');
      this.endScreen = document.getElementById('end-screen');

      // HUD References
      this.hudScore = document.getElementById('hud-score');
      this.hudBest = document.getElementById('hud-best');
      this.hudLength = document.getElementById('hud-length');
      this.hudTime = document.getElementById('hud-time');
      this.hudOpponents = document.getElementById('hud-opponents');
      this.hudSpeed = document.getElementById('hud-speed');
      this.opponentsLegend = document.getElementById('opponents-legend');

      // State Variables
      this.state = 'MENU'; // 'MENU' | 'PLAYING' | 'PAUSED' | 'GAME_OVER' | 'VICTORY'
      this.playerColor = '#00ff88';
      this.fruitColor = '#ff0055';
      this.opponentCount = 3;
      this.speedMode = 'Normal';

      this.player = null;
      this.opponents = [];
      this.fruits = []; // { x, y, type: 'regular'|'corpse', points, color }
      this.score = 0;
      this.highScore = parseInt(localStorage.getItem('snake_battle_best') || '0', 10);
      this.hudBest.textContent = this.highScore;

      this.gameStartTime = 0;
      this.elapsedSeconds = 0;
      this.timerInterval = null;
      this.gameLoopTimeout = null;

      this.setupDOM();
      this.setupControls();
      this.render();
    }

    setupDOM() {
      // Color pickers & chips
      const playerColorInput = document.getElementById('player-color-picker');
      const fruitColorInput = document.getElementById('fruit-color-picker');

      playerColorInput.addEventListener('input', (e) => {
        this.playerColor = e.target.value;
      });

      fruitColorInput.addEventListener('input', (e) => {
        this.fruitColor = e.target.value;
      });

      // Preset chips for player color
      document.querySelectorAll('#player-color-picker ~ .preset-colors .color-chip').forEach(chip => {
        chip.addEventListener('click', () => {
          document.querySelectorAll('#player-color-picker ~ .preset-colors .color-chip').forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          this.playerColor = chip.dataset.color;
          playerColorInput.value = this.playerColor;
        });
      });

      // Preset chips for fruit color
      document.querySelectorAll('#fruit-color-picker ~ .preset-colors .color-chip').forEach(chip => {
        chip.addEventListener('click', () => {
          document.querySelectorAll('#fruit-color-picker ~ .preset-colors .color-chip').forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          this.fruitColor = chip.dataset.color;
          fruitColorInput.value = this.fruitColor;
        });
      });

      // Opponents Segmented Control
      const oppButtons = document.querySelectorAll('#opponents-selector .seg-btn');
      oppButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          oppButtons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          this.opponentCount = parseInt(btn.dataset.value, 10);
        });
      });

      // Speed Segmented Control
      const speedButtons = document.querySelectorAll('#speed-selector .seg-btn');
      speedButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          speedButtons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          this.speedMode = btn.dataset.value;
        });
      });

      // Action Buttons
      document.getElementById('btn-start-battle').addEventListener('click', () => {
        this.sound.playClick();
        this.startGame();
      });

      document.getElementById('btn-pause').addEventListener('click', () => {
        this.togglePause();
      });

      document.getElementById('btn-resume').addEventListener('click', () => {
        this.togglePause();
      });

      document.getElementById('btn-sound').addEventListener('click', (e) => {
        const enabled = this.sound.toggle();
        e.currentTarget.querySelector('.label').textContent = enabled ? 'SOUND: ON' : 'SOUND: OFF';
        e.currentTarget.querySelector('.icon').textContent = enabled ? '🔊' : '🔇';
      });

      document.getElementById('btn-restart').addEventListener('click', () => {
        this.sound.playClick();
        this.startGame();
      });

      document.getElementById('btn-play-again').addEventListener('click', () => {
        this.sound.playClick();
        this.startGame();
      });

      document.getElementById('btn-lobby').addEventListener('click', () => {
        this.sound.playClick();
        this.showLobby();
      });
    }

    setupControls() {
      // Keyboard input
      window.addEventListener('keydown', (e) => {
        // Prevent window scroll on arrow / space
        if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(e.key)) {
          e.preventDefault();
        }

        if (e.key === ' ' || e.key === 'p' || e.key === 'P') {
          if (this.state === 'PLAYING' || this.state === 'PAUSED') {
            this.togglePause();
          }
          return;
        }

        if (e.key === 'r' || e.key === 'R') {
          if (this.state === 'PLAYING' || this.state === 'GAME_OVER' || this.state === 'VICTORY') {
            this.startGame();
          }
          return;
        }

        if (e.key === 'm' || e.key === 'M') {
          document.getElementById('btn-sound').click();
          return;
        }

        if (this.state !== 'PLAYING' || !this.player || !this.player.isAlive) return;

        switch (e.key) {
          case 'ArrowUp':
          case 'w':
          case 'W':
            this.player.setDirection({ x: 0, y: -1 });
            break;
          case 'ArrowDown':
          case 's':
          case 'S':
            this.player.setDirection({ x: 0, y: 1 });
            break;
          case 'ArrowLeft':
          case 'a':
          case 'A':
            this.player.setDirection({ x: -1, y: 0 });
            break;
          case 'ArrowRight':
          case 'd':
          case 'D':
            this.player.setDirection({ x: 1, y: 0 });
            break;
        }
      });

      // Mobile Touch D-Pad
      const bindTouch = (id, dir) => {
        const btn = document.getElementById(id);
        const handleAction = (e) => {
          e.preventDefault();
          if (this.state === 'PLAYING' && this.player && this.player.isAlive) {
            this.player.setDirection(dir);
            this.sound.init();
          }
        };
        btn.addEventListener('touchstart', handleAction, { passive: false });
        btn.addEventListener('mousedown', handleAction);
      };

      bindTouch('touch-up', { x: 0, y: -1 });
      bindTouch('touch-down', { x: 0, y: 1 });
      bindTouch('touch-left', { x: -1, y: 0 });
      bindTouch('touch-right', { x: 1, y: 0 });
    }

    showLobby() {
      this.state = 'MENU';
      clearTimeout(this.gameLoopTimeout);
      clearInterval(this.timerInterval);
      this.startScreen.classList.add('active');
      this.pauseScreen.classList.remove('active');
      this.endScreen.classList.remove('active');
    }

    startGame() {
      clearTimeout(this.gameLoopTimeout);
      clearInterval(this.timerInterval);

      this.state = 'PLAYING';
      this.score = 0;
      this.elapsedSeconds = 0;
      this.fruits = [];
      this.particles.particles = [];

      // Hide all overlays
      this.startScreen.classList.remove('active');
      this.pauseScreen.classList.remove('active');
      this.endScreen.classList.remove('active');

      // Update HUD static indicators
      this.hudScore.textContent = '0';
      this.hudLength.textContent = '4';
      this.hudTime.textContent = '00:00';
      this.hudOpponents.textContent = this.opponentCount;
      this.hudSpeed.textContent = this.speedMode;

      // 1. Initialize Player Snake
      this.player = new Snake(
        'player',
        'Player',
        this.playerColor,
        [
          { x: 6, y: GRID_SIZE - 8 },
          { x: 5, y: GRID_SIZE - 8 },
          { x: 4, y: GRID_SIZE - 8 },
          { x: 3, y: GRID_SIZE - 8 }
        ],
        { x: 1, y: 0 },
        false
      );

      // 2. Initialize AI Opponents
      this.opponents = [];
      for (let i = 0; i < this.opponentCount; i++) {
        const conf = AI_PRESETS[i % AI_PRESETS.length];
        const segments = [{ x: conf.startX, y: conf.startY }];
        const rev = { x: -conf.dir.x, y: -conf.dir.y };
        for (let s = 1; s <= 3; s++) {
          segments.push({ x: conf.startX + rev.x * s, y: conf.startY + rev.y * s });
        }
        const ai = new Snake(conf.id, conf.name, conf.color, segments, conf.dir, true);
        ai.behavior = conf.behavior;
        this.opponents.push(ai);
      }

      // Render opponent badges in legend
      this.renderOpponentsLegend();

      // 3. Pre-populate arena with 5 initial fruits
      for (let i = 0; i < 5; i++) {
        this.spawnFruit(this.fruitColor);
      }

      // Start elapsed timer
      this.gameStartTime = Date.now();
      this.timerInterval = setInterval(() => {
        if (this.state === 'PLAYING') {
          this.elapsedSeconds++;
          const mins = String(Math.floor(this.elapsedSeconds / 60)).padStart(2, '0');
          const secs = String(this.elapsedSeconds % 60).padStart(2, '0');
          this.hudTime.textContent = `${mins}:${secs}`;
        }
      }, 1000);

      // Begin Tick Cycle
      this.tick();
    }

    renderOpponentsLegend() {
      this.opponentsLegend.innerHTML = '';
      this.opponents.forEach(ai => {
        const badge = document.createElement('div');
        badge.className = `legend-badge ${ai.isAlive ? '' : 'dead'}`;
        badge.id = `legend-${ai.id}`;
        badge.innerHTML = `
          <span class="legend-dot" style="background:${ai.color}; box-shadow: 0 0 6px ${ai.color}"></span>
          <span>${ai.name} (${ai.behavior})</span>
        `;
        this.opponentsLegend.appendChild(badge);
      });
    }

    togglePause() {
      if (this.state === 'PLAYING') {
        this.state = 'PAUSED';
        this.pauseScreen.classList.add('active');
        clearTimeout(this.gameLoopTimeout);
      } else if (this.state === 'PAUSED') {
        this.state = 'PLAYING';
        this.pauseScreen.classList.remove('active');
        this.tick();
      }
    }

    spawnFruit(color = '#ff0055', type = 'regular', points = 10, forcedPos = null) {
      if (forcedPos) {
        this.fruits.push({
          x: forcedPos.x,
          y: forcedPos.y,
          type: type,
          points: points,
          color: color
        });
        return;
      }

      // Find unoccupied cell
      const occupied = new Set();
      const allSnakes = [this.player, ...this.opponents];
      allSnakes.forEach(s => {
        if (s && s.isAlive) {
          s.segments.forEach(seg => occupied.add(`${seg.x},${seg.y}`));
        }
      });
      this.fruits.forEach(f => occupied.add(`${f.x},${f.y}`));

      const available = [];
      for (let x = 0; x < GRID_SIZE; x++) {
        for (let y = 0; y < GRID_SIZE; y++) {
          if (!occupied.has(`${x},${y}`)) {
            available.push({ x, y });
          }
        }
      }

      if (available.length > 0) {
        const choice = available[Math.floor(Math.random() * available.length)];
        this.fruits.push({
          x: choice.x,
          y: choice.y,
          type: type,
          points: points,
          color: color
        });
      }
    }

    tick() {
      if (this.state !== 'PLAYING') return;

      this.updateGameLogic();
      this.render();

      const delay = SPEED_CONFIG[this.speedMode] || 105;
      this.gameLoopTimeout = setTimeout(() => this.tick(), delay);
    }

    updateGameLogic() {
      const allSnakes = [this.player, ...this.opponents];

      // 1. AI Decision Making
      this.opponents.forEach(ai => {
        if (ai.isAlive) {
          this.decideAIMove(ai);
        }
      });

      // 2. Advance all alive snakes forward
      allSnakes.forEach(s => {
        if (s && s.isAlive) {
          s.move();
        }
      });

      // 3. Collision Detection
      const fatalSnakes = new Set();
      const aliveSnakes = allSnakes.filter(s => s && s.isAlive);

      // Check wall & self collision
      aliveSnakes.forEach(s => {
        const h = s.head;
        // Wall bounds
        if (h.x < 0 || h.x >= GRID_SIZE || h.y < 0 || h.y >= GRID_SIZE) {
          fatalSnakes.add(s);
          return;
        }
        // Self collision
        for (let i = 1; i < s.segments.length; i++) {
          if (h.x === s.segments[i].x && h.y === s.segments[i].y) {
            fatalSnakes.add(s);
            return;
          }
        }
      });

      // Inter-snake body and head collisions
      for (let i = 0; i < aliveSnakes.length; i++) {
        for (let j = 0; j < aliveSnakes.length; j++) {
          if (i === j) continue;
          const snakeA = aliveSnakes[i];
          const snakeB = aliveSnakes[j];

          // Snake A head hits Snake B body
          for (let segIdx = 0; segIdx < snakeB.segments.length; segIdx++) {
            const seg = snakeB.segments[segIdx];
            if (snakeA.head.x === seg.x && snakeA.head.y === seg.y) {
              if (segIdx === 0) {
                // Head to head clash: both perish
                fatalSnakes.add(snakeA);
                fatalSnakes.add(snakeB);
              } else {
                fatalSnakes.add(snakeA);
                snakeB.kills++;
              }
            }
          }
        }
      }

      // 4. Process Snake Deaths & Rule 5: Dead Snake -> Fruit Conversion!
      fatalSnakes.forEach(deadSnake => {
        if (deadSnake.isAlive) {
          deadSnake.die();
          this.sound.playDeath();
          this.particles.emit(deadSnake.head.x, deadSnake.head.y, deadSnake.color, 24, 1.8);

          // Update legend badge
          const badge = document.getElementById(`legend-${deadSnake.id}`);
          if (badge) badge.classList.add('dead');

          // RULE 5: Convert all body segments into high-value corpse fruits!
          const corpseSegments = deadSnake.convertToFruits();
          corpseSegments.forEach(seg => {
            if (seg.x >= 0 && seg.x < GRID_SIZE && seg.y >= 0 && seg.y < GRID_SIZE) {
              this.spawnFruit(deadSnake.color, 'corpse', 15, seg);
              this.particles.emit(seg.x, seg.y, deadSnake.color, 4, 0.8);
            }
          });

          // If AI was killed and player survived, award player elimination bonus
          if (deadSnake.isAI && this.player.isAlive) {
            this.score += 50;
            this.hudScore.textContent = this.score;
          }
        }
      });

      // Check Player Death
      if (!this.player.isAlive) {
        this.triggerGameOver(false);
        return;
      }

      // Check Victory Condition (All AI opponents eliminated)
      const aliveOpponents = this.opponents.filter(o => o.isAlive);
      this.hudOpponents.textContent = aliveOpponents.length;

      if (aliveOpponents.length === 0 && this.opponents.length > 0) {
        this.triggerGameOver(true);
        return;
      }

      // 5. Fruit Consumption & Snake Growth
      allSnakes.forEach(s => {
        if (!s || !s.isAlive) return;

        for (let fIdx = this.fruits.length - 1; fIdx >= 0; fIdx--) {
          const f = this.fruits[fIdx];
          if (s.head.x === f.x && s.head.y === f.y) {
            // Snake eats fruit
            s.grow(1);
            this.fruits.splice(fIdx, 1);
            this.particles.emit(f.x, f.y, f.color, 10, 1.2);

            if (!s.isAI) {
              this.sound.playEat();
              this.score += f.points;
              this.hudScore.textContent = this.score;
              this.hudLength.textContent = this.player.length;

              if (this.score > this.highScore) {
                this.highScore = this.score;
                this.hudBest.textContent = this.highScore;
                localStorage.setItem('snake_battle_best', String(this.highScore));
              }
            }
          }
        }
      });

      // 6. Maintain minimum regular fruit count on field
      const regularFruitCount = this.fruits.filter(f => f.type === 'regular').length;
      if (regularFruitCount < 4) {
        this.spawnFruit(this.fruitColor);
      }
    }

    /**
     * AI Navigation Decision Heuristic
     */
    decideAIMove(ai) {
      const candidates = [
        { x: 0, y: -1 }, // UP
        { x: 0, y: 1 },  // DOWN
        { x: -1, y: 0 }, // LEFT
        { x: 1, y: 0 }   // RIGHT
      ];

      const allSnakes = [this.player, ...this.opponents];
      const validMoves = [];

      for (const d of candidates) {
        // Prevent reverse
        if (ai.dir.x + d.x === 0 && ai.dir.y + d.y === 0) continue;

        const target = { x: ai.head.x + d.x, y: ai.head.y + d.y };

        // Out of bounds check
        if (target.x < 0 || target.x >= GRID_SIZE || target.y < 0 || target.y >= GRID_SIZE) continue;

        // Self body collision
        if (ai.segments.some(seg => seg.x === target.x && seg.y === target.y)) continue;

        // Opponents body collision
        let collidesOther = false;
        for (const other of allSnakes) {
          if (other && other.isAlive && other.id !== ai.id) {
            if (other.segments.some(seg => seg.x === target.x && seg.y === target.y)) {
              collidesOther = true;
              break;
            }
          }
        }
        if (collidesOther) continue;

        validMoves.push(d);
      }

      if (validMoves.length === 0) return; // Trapped, let it take its inevitable step

      // Evaluate moves according to AI Behavior
      let bestMove = validMoves[0];
      let bestScore = -Infinity;

      // Find nearest fruit
      let nearestFruit = null;
      let minFruitDist = Infinity;
      for (const f of this.fruits) {
        const dist = Math.abs(ai.head.x - f.x) + Math.abs(ai.head.y - f.y);
        if (dist < minFruitDist) {
          minFruitDist = dist;
          nearestFruit = f;
        }
      }

      for (const d of validMoves) {
        const nextPos = { x: ai.head.x + d.x, y: ai.head.y + d.y };
        let moveScore = 0;

        // 1. Fruit Attraction
        if (nearestFruit) {
          const distToFruit = Math.abs(nextPos.x - nearestFruit.x) + Math.abs(nextPos.y - nearestFruit.y);
          moveScore += (80 - distToFruit * 2.5);
          // High bonus for corpse fruits
          if (nearestFruit.type === 'corpse') {
            moveScore += 30;
          }
        }

        // 2. Wall Distance Margin
        const wallMargin = Math.min(nextPos.x, GRID_SIZE - 1 - nextPos.x, nextPos.y, GRID_SIZE - 1 - nextPos.y);

        // 3. Behavior Personality
        if (ai.behavior === 'Cautious') {
          if (wallMargin < 2) moveScore -= 60;
          // Avoid close heads
          allSnakes.forEach(other => {
            if (other && other.isAlive && other.id !== ai.id) {
              const dHead = Math.abs(nextPos.x - other.head.x) + Math.abs(nextPos.y - other.head.y);
              if (dHead <= 2) moveScore -= 80;
            }
          });
        } else if (ai.behavior === 'Aggressive') {
          if (this.player && this.player.isAlive) {
            const dPlayer = Math.abs(nextPos.x - this.player.head.x) + Math.abs(nextPos.y - this.player.head.y);
            if (ai.length >= this.player.length) {
              moveScore += (50 - dPlayer * 1.8);
            } else {
              moveScore -= (30 - dPlayer);
            }
          }
        } else {
          // Balanced
          if (wallMargin < 1) moveScore -= 25;
        }

        // 4. Open neighbor lookahead
        let openExits = 0;
        for (const testD of candidates) {
          const p = { x: nextPos.x + testD.x, y: nextPos.y + testD.y };
          if (p.x >= 0 && p.x < GRID_SIZE && p.y >= 0 && p.y < GRID_SIZE) {
            openExits++;
          }
        }
        moveScore += openExits * 8;

        // Momentum preference
        if (d.x === ai.dir.x && d.y === ai.dir.y) {
          moveScore += 4;
        }

        if (moveScore > bestScore) {
          bestScore = moveScore;
          bestMove = d;
        }
      }

      ai.setDirection(bestMove);
    }

    triggerGameOver(isVictory) {
      this.state = isVictory ? 'VICTORY' : 'GAME_OVER';
      clearTimeout(this.gameLoopTimeout);
      clearInterval(this.timerInterval);

      if (isVictory) {
        this.sound.playVictory();
      } else {
        this.sound.playDeath();
      }

      const endTitle = document.getElementById('end-title');
      const endSubtitle = document.getElementById('end-subtitle');
      const finalScore = document.getElementById('end-final-score');
      const finalLength = document.getElementById('end-final-length');
      const finalKills = document.getElementById('end-final-kills');
      const finalTime = document.getElementById('end-final-time');

      if (isVictory) {
        endTitle.textContent = 'VICTORY ROYALE!';
        endTitle.style.color = '#00ff88';
        endSubtitle.textContent = 'You conquered the arena and outplayed all rivals!';
      } else {
        endTitle.textContent = 'GAME OVER';
        endTitle.style.color = '#ff0055';
        endSubtitle.textContent = 'A fatal collision took you down!';
      }

      finalScore.textContent = this.score;
      finalLength.textContent = this.player ? this.player.length : 4;
      finalKills.textContent = this.player ? this.player.kills : 0;
      finalTime.textContent = this.hudTime.textContent;

      this.endScreen.classList.add('active');
    }

    // --- Rendering Pipeline ---
    render() {
      this.ctx.clearRect(0, 0, BASE_CANVAS_SIZE, BASE_CANVAS_SIZE);

      // 1. Draw subtle grid background
      this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.025)';
      this.ctx.lineWidth = 1;
      for (let x = 0; x <= BASE_CANVAS_SIZE; x += CELL_SIZE) {
        this.ctx.beginPath();
        this.ctx.moveTo(x, 0);
        this.ctx.lineTo(x, BASE_CANVAS_SIZE);
        this.ctx.stroke();
      }
      for (let y = 0; y <= BASE_CANVAS_SIZE; y += CELL_SIZE) {
        this.ctx.beginPath();
        this.ctx.moveTo(0, y);
        this.ctx.lineTo(BASE_CANVAS_SIZE, y);
        this.ctx.stroke();
      }

      // 2. Draw Fruits
      this.fruits.forEach(f => {
        const cx = f.x * CELL_SIZE + CELL_SIZE / 2;
        const cy = f.y * CELL_SIZE + CELL_SIZE / 2;
        const radius = (CELL_SIZE / 2) * (f.type === 'corpse' ? 0.7 : 0.65);

        this.ctx.save();
        this.ctx.shadowColor = f.color;
        this.ctx.shadowBlur = f.type === 'corpse' ? 14 : 10;
        this.ctx.fillStyle = f.color;

        this.ctx.beginPath();
        this.ctx.arc(cx, cy, radius, 0, Math.PI * 2);
        this.ctx.fill();

        // Inner glowing core
        this.ctx.fillStyle = '#ffffff';
        this.ctx.beginPath();
        this.ctx.arc(cx - radius * 0.2, cy - radius * 0.2, radius * 0.35, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.restore();
      });

      // 3. Draw All Snakes
      const allSnakes = [...this.opponents];
      if (this.player) allSnakes.push(this.player);

      allSnakes.forEach(s => {
        if (!s || !s.isAlive || s.segments.length === 0) return;

        // Draw body segments
        for (let i = s.segments.length - 1; i >= 0; i--) {
          const seg = s.segments[i];
          const px = seg.x * CELL_SIZE;
          const py = seg.y * CELL_SIZE;
          const isHead = i === 0;

          this.ctx.save();
          if (isHead) {
            this.ctx.fillStyle = s.color;
            this.ctx.shadowColor = s.color;
            this.ctx.shadowBlur = 12;

            // Rounded head rectangle
            this.roundRect(this.ctx, px + 1, py + 1, CELL_SIZE - 2, CELL_SIZE - 2, 5);
            this.ctx.fill();

            // Draw glowing snake eyes
            this.ctx.fillStyle = '#080b11';
            let eye1X, eye1Y, eye2X, eye2Y;
            if (s.dir.x === 1) { // Moving Right
              eye1X = px + 13; eye1Y = py + 5;
              eye2X = px + 13; eye2Y = py + 15;
            } else if (s.dir.x === -1) { // Moving Left
              eye1X = px + 7; eye1Y = py + 5;
              eye2X = px + 7; eye2Y = py + 15;
            } else if (s.dir.y === -1) { // Moving Up
              eye1X = px + 5; eye1Y = py + 7;
              eye2X = px + 15; eye2Y = py + 7;
            } else { // Moving Down
              eye1X = px + 5; eye1Y = py + 13;
              eye2X = px + 15; eye2Y = py + 13;
            }

            this.ctx.beginPath();
            this.ctx.arc(eye1X, eye1Y, 2.5, 0, Math.PI * 2);
            this.ctx.arc(eye2X, eye2Y, 2.5, 0, Math.PI * 2);
            this.ctx.fill();

            // Eye reflection
            this.ctx.fillStyle = '#ffffff';
            this.ctx.beginPath();
            this.ctx.arc(eye1X - 0.5, eye1Y - 0.5, 1, 0, Math.PI * 2);
            this.ctx.arc(eye2X - 0.5, eye2Y - 0.5, 1, 0, Math.PI * 2);
            this.ctx.fill();

          } else {
            // Body segment with slight taper / opacity gradient
            const alpha = 0.5 + (0.5 * (1 - i / s.segments.length));
            this.ctx.fillStyle = s.color;
            this.ctx.globalAlpha = alpha;
            this.roundRect(this.ctx, px + 2, py + 2, CELL_SIZE - 4, CELL_SIZE - 4, 4);
            this.ctx.fill();
          }
          this.ctx.restore();
        }
      });

      // 4. Update and render particle physics
      this.particles.update();
      this.particles.draw(this.ctx);
    }

    roundRect(ctx, x, y, width, height, radius) {
      ctx.beginPath();
      ctx.moveTo(x + radius, y);
      ctx.lineTo(x + width - radius, y);
      ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
      ctx.lineTo(x + width, y + height - radius);
      ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
      ctx.lineTo(x + radius, y + height);
      ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
      ctx.lineTo(x, y + radius);
      ctx.quadraticCurveTo(x, y, x + radius, y);
      ctx.closePath();
    }
  }

  // Auto-boot when DOM is loaded
  window.addEventListener('DOMContentLoaded', () => {
    window.gameEngine = new SnakeBattleEngine();
  });

})();
