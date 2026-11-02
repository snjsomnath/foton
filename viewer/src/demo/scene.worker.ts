import { prepareGeometry, prepareColors, type PrepareRequest, type PrepareResponse } from './scenePreparation';
const worker = self as unknown as { onmessage: ((event: MessageEvent<PrepareRequest>) => void) | null; postMessage: (message: PrepareResponse, transfer: Transferable[]) => void };
worker.onmessage = ({ data }) => {
  try {
    const geometry = data.geometry ? prepareGeometry({ ...data.frame, geometry: data.geometry }) : undefined;
    const colors = prepareColors(data.frame, data.metric);
    const transfer: Transferable[] = [colors.buffer];
    if (geometry) {
      transfer.push(geometry.cells.buffer);
      geometry.surfaces.forEach(surface => transfer.push(surface.positions.buffer, surface.normals.buffer, surface.edges.buffer));
    }
    worker.postMessage({id: data.id, key: data.key, geometry, colors}, transfer);
  } catch (reason) { worker.postMessage({id: data.id, key: data.key, error: String(reason)}, []); }
};
