(() => {
  const form = document.getElementById('quoteForm');
  if (!form) {
    return;
  }

  const fields = {
    customer: document.getElementById('customerName'),
    contact: document.getElementById('contactPerson'),
    projectRef: document.getElementById('projectRef'),
    quantity: document.getElementById('quantity'),
    machineRate: document.getElementById('machineRate'),
    materialCost: document.getElementById('materialCost'),
    materialMarkup: document.getElementById('materialMarkup'),
    profitMargin: document.getElementById('profitMargin'),
    deliveryWeeks: document.getElementById('deliveryWeeks'),
  };

  const output = document.getElementById('quoteOutput');
  const status = document.getElementById('quoteStatus');
  const quoteDate = document.getElementById('quoteDate');
  const quoteValidUntil = document.getElementById('quoteValidUntil');
  const quoteCustomer = document.getElementById('quoteCustomer');
  const quoteContact = document.getElementById('quoteContact');
  const quoteProjectRef = document.getElementById('quoteProjectRef');
  const quoteDelivery = document.getElementById('quoteDelivery');
  const quoteTableBody = document.getElementById('quoteTableBody');
  const quoteSubtotal = document.getElementById('quoteSubtotal');
  const quoteSetup = document.getElementById('quoteSetup');
  const quoteNet = document.getElementById('quoteNet');
  const quoteVat = document.getElementById('quoteVat');
  const quoteGross = document.getElementById('quoteGross');
  const printButton = document.getElementById('printQuote');
  const copyButton = document.getElementById('copyQuote');

  const currencyFormatter = new Intl.NumberFormat('de-DE', {
    style: 'currency',
    currency: 'EUR',
  });
  const numberFormatter = new Intl.NumberFormat('de-DE', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });

  const safeNumber = (value, fallback, { min = 0, max = Number.POSITIVE_INFINITY } = {}) => {
    const parsed = Number(String(value).replace(',', '.'));
    if (!Number.isFinite(parsed)) {
      return fallback;
    }
    return Math.min(Math.max(parsed, min), max);
  };

  const safeInteger = (value, fallback, { min = 1, max = Number.POSITIVE_INFINITY } = {}) => {
    const parsed = Number.parseInt(String(value).replace(',', '.'), 10);
    if (!Number.isFinite(parsed)) {
      return fallback;
    }
    return Math.min(Math.max(parsed, min), max);
  };

  const safeText = (value, fallback) => {
    const trimmed = value.trim();
    return trimmed.length ? trimmed : fallback;
  };

  const updateStatus = (message) => {
    if (status) {
      status.textContent = message;
    }
  };

  const setOutputVisible = (visible) => {
    output.classList.toggle('is-visible', visible);
    output.hidden = !visible;
  };

  const formatCurrency = (value) => currencyFormatter.format(value);
  const formatNumber = (value) => numberFormatter.format(value);

  const buildRow = ({ position, description, quantity, unit, unitPrice, totalPrice, muted = false }) => {
    const row = document.createElement('tr');
    if (muted) {
      row.classList.add('quote-row-muted');
    }

    const createCell = (text, className) => {
      const cell = document.createElement('td');
      if (className) {
        cell.className = className;
      }
      cell.textContent = text;
      return cell;
    };

    row.appendChild(createCell(position));

    const descriptionCell = document.createElement('td');
    descriptionCell.innerHTML = description;
    row.appendChild(descriptionCell);

    row.appendChild(createCell(quantity));
    row.appendChild(createCell(unit));

    const unitCell = createCell(unitPrice, 'price-cell');
    const totalCell = createCell(totalPrice, 'price-cell');

    row.appendChild(unitCell);
    row.appendChild(totalCell);

    return row;
  };

  const generateQuote = () => {
    if (!form.reportValidity()) {
      updateStatus('Bitte fehlende Pflichtfelder ergänzen.');
      return;
    }

    const customer = safeText(fields.customer.value, '[Kunde eintragen]');
    const contact = safeText(fields.contact.value, '[Ansprechpartner]');
    const project = safeText(fields.projectRef.value, '[Anfrage-Nr.]');
    const qty = safeInteger(fields.quantity.value, 10, { min: 1 });
    const machineRate = safeNumber(fields.machineRate.value, 85, { min: 0 });
    const materialCost = safeNumber(fields.materialCost.value, 45, { min: 0 });
    const materialMarkup = safeNumber(fields.materialMarkup.value, 15, { min: 0, max: 200 });
    const profitMargin = safeNumber(fields.profitMargin.value, 20, { min: 0, max: 200 });
    const deliveryWeeks = safeInteger(fields.deliveryWeeks.value, 3, { min: 1, max: 52 });

    const timePerPart = 41.8;
    const setupTime = 30;
    const machiningCostPerPart = (timePerPart / 60) * machineRate;
    const materialWithMarkup = materialCost * (1 + materialMarkup / 100);
    const costPerPart = machiningCostPerPart + materialWithMarkup;
    const pricePerPart = costPerPart * (1 + profitMargin / 100);
    const setupCost = (setupTime / 60) * machineRate;

    const subtotal = pricePerPart * qty;
    const netTotal = subtotal + setupCost;
    const vat = netTotal * 0.19;
    const grossTotal = netTotal + vat;

    const today = new Date();
    const validUntil = new Date(today);
    validUntil.setDate(validUntil.getDate() + 30);

    quoteDate.textContent = today.toLocaleDateString('de-DE');
    quoteValidUntil.textContent = validUntil.toLocaleDateString('de-DE');
    quoteCustomer.textContent = customer;
    quoteContact.textContent = contact;
    quoteProjectRef.textContent = project;
    quoteDelivery.textContent = `${deliveryWeeks} Wochen`;

    quoteTableBody.innerHTML = '';

    quoteTableBody.appendChild(
      buildRow({
        position: '1',
        description:
          '<strong>Grundplatte (Zahnradpumpe)</strong><br><span class="text-muted">Zeichnung WCAD-15-02-2020, Werkstoff 1.4571</span>',
        quantity: String(qty),
        unit: 'Stück',
        unitPrice: formatNumber(pricePerPart),
        totalPrice: formatNumber(subtotal),
      })
    );

    quoteTableBody.appendChild(
      buildRow({
        position: '2',
        description: 'Material: Edelstahl 1.4571, Rohteil Ø135×50mm',
        quantity: String(qty),
        unit: 'Stück',
        unitPrice: 'inkl.',
        totalPrice: 'inkl.',
        muted: true,
      })
    );

    quoteTableBody.appendChild(
      buildRow({
        position: '3',
        description: `CNC-Bearbeitung FEHLMANN VERSA® 943 (${formatNumber(timePerPart)} min/Stück)`,
        quantity: String(qty),
        unit: 'Stück',
        unitPrice: 'inkl.',
        totalPrice: 'inkl.',
        muted: true,
      })
    );

    quoteSubtotal.textContent = formatCurrency(subtotal);
    quoteSetup.textContent = formatCurrency(setupCost);
    quoteNet.textContent = formatCurrency(netTotal);
    quoteVat.textContent = formatCurrency(vat);
    quoteGross.textContent = formatCurrency(grossTotal);

    setOutputVisible(true);
    updateStatus('Angebot aktualisiert.');

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!prefersReducedMotion) {
      output.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  const copyQuote = async () => {
    const quoteText = output.innerText.trim();
    if (!quoteText) {
      updateStatus('Kein Angebot zum Kopieren verfügbar.');
      return;
    }

    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(quoteText);
      } else {
        const textArea = document.createElement('textarea');
        textArea.value = quoteText;
        textArea.style.position = 'fixed';
        textArea.style.opacity = '0';
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
      }
      updateStatus('Angebot in die Zwischenablage kopiert.');
    } catch (error) {
      updateStatus('Kopieren fehlgeschlagen. Bitte manuell markieren und kopieren.');
    }
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    generateQuote();
  });

  if (printButton) {
    printButton.addEventListener('click', () => window.print());
  }

  if (copyButton) {
    copyButton.addEventListener('click', () => copyQuote());
  }

  setOutputVisible(false);
  updateStatus('Bereit für die Angebotserstellung.');
})();
